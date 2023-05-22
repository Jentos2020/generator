from datetime import timedelta
from .yesterday_info import allValue
from ..serializers import DayStatSerializer, DaysSumSerializer, ShopStatSerializer
from ..models import ShopState, DayStat
from django.utils import timezone
from django.core.cache import cache
from django.db.models.functions import Trunc
from django.db.models import Sum
from django.db.models import BigIntegerField, ExpressionWrapper


def dashStat(allDaysStat, days):
    data = dict()
    # вытаскивает сумму по каждой категории за каждый день
    period = timezone.now() - timedelta(days=allDaysStat)
    daysStat = DayStat.objects.filter(time_update__gte=period) \
        .annotate(day=Trunc('time_update', 'day')) \
        .values('day') \
        .annotate(BM_count=Sum('BM_count'), BM_cost=Sum('BM_cost'),
                  ZRD_count=Sum('ZRD_count'), ZRD_cost=Sum('ZRD_cost'),
                  Farm_count=Sum('Farm_count'), Farm_cost=Sum('Farm_cost'),
                  Autoreg_count=Sum('Autoreg_count'), Autoreg_cost=Sum('Autoreg_cost'),
                  FP_count=Sum('FP_count'), FP_cost=Sum('FP_cost'),
                  PZRDFP_count=Sum('PZRDFP_count'), PZRDFP_cost=Sum('PZRDFP_cost'),
                  Undef_count=Sum('Undef_count'), Undef_cost=Sum('Undef_cost')
                  ) \
        .order_by('-day')


    # Категория с самым большим оборотом
    today = timezone.now().date()
    catInterpreter = {'BM_cost': 'БМ+', 'ZRD_cost': 'ЗРД+', 'Farm_cost': 'Фармы', 'Autoreg_cost': 'Автореги',
                      'FP_cost': 'ФП', 'PZRDFP_cost': 'ПЗРДФП', 'Undef_cost': 'Остальное', }
    todayMax = filter(lambda x: x['day'].date() == today, daysStat)
    values_list = list(todayMax)
    spendList = [value for key, value in values_list[0].items()
                 if key.endswith('_cost')]
    todayMaxSoldCat = max(spendList)
    todaySum = sum(spendList)
    # топ категория за сегодня
    data['bestCatToday'] = catInterpreter[[k for k, v in values_list[0].items(
    ) if v == todayMaxSoldCat][0]]
    # процент от общей суммы проданного
    data['bestCatTodayPercent'] = round((todayMaxSoldCat / todaySum) * 100, 2)

    # средняя цена сегодня
    countList = [value for key, value in values_list[0].items()
                 if key.endswith('_count')]
    todayCount = sum(countList)
    data['averagePrice'] = todaySum // todayCount
    cache.set('cur_price', data['averagePrice'], 60*60*24)

    # на сколько изменилась средняя цена со вчера
    yestPrice = cache.get('yest_price')
    if yestPrice:
        data['priceDiff'] = round(((data['averagePrice'] - yestPrice) / yestPrice) * 100, 2)
    else:
        data['priceDiff'] = 0
 
    # Продажи по категориям по дням
    serializer = DayStatSerializer(daysStat, many=True)
    data['days'] = serializer.data

    # Вытаскиваем данные по магазам за сегодня
    todayStat = ShopState.objects.select_related('shop').all()
    data['shops'] = ShopStatSerializer(todayStat, many=True).data

    # Считаем текущий объем рынка (сумма) и сумму уже проданного сегодня:
    # data['totalSoldToday'] = sum(
    #     value for key, value in daysStat[0].items() if key.endswith('_cost'))

    # подсчет текущего объема всех товаров
    data['totalValue'] = allValue()
    
    # объем всего рынка сегодня по сравнению со вчера
    yestValue = cache.get('yest_value')
    if yestValue:
        valueDiff = round(((data['totalValue'] - yestValue) / yestValue) * 100, 2)
    else: 
        valueDiff = 0
    data['valueDiff'] = valueDiff

    # Достаем данные за N дней:
    for dicts in daysStat[1:days]:
        for key in daysStat[0]:
            if key == 'day':
                continue
            daysStat[0][key] += dicts[key]

    serializer = DaysSumSerializer(daysStat[0])
    data['totalDaysCatSum'] = serializer.data

    # Считаем за текущий и предыдущий отчетный период в N дней
    curDaysSumCost = 0
    prevDaysSumCost = 0
    for key in daysStat[0]:
        if key.endswith('_cost'):
            curDaysSumCost += daysStat[0][key]
    # предыдущие N дней:
    for dicts in daysStat[days:days*2]:
        for key in dicts:
            if key == 'day':
                continue
            prevDaysSumCost += dicts[key]
    data['curDaysSumCost'] = curDaysSumCost
    data['prevDaysSumDiff'] = round(((curDaysSumCost - prevDaysSumCost) / prevDaysSumCost) * 100, 2)
    return data
