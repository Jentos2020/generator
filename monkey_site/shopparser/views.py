from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .logic.dashboard import dashStat
from .tasks import taskUpadteDB
from django.core.cache import cache
from .logic.yesterday_info import updateYesterdayInfo


def shopParse(request):
    taskUpadteDB.delay()
    # updateYesterdayInfo()
    return render(request, 'index.html', {'data': 'Начал выполнять'})


def statView(request):
    allDaysStat = 50
    days = 7
    if request.method == 'GET':
        data = cache.get('dash_data')
        if not data:
            data = dashStat(allDaysStat, days)
            cache.set('dash_data', data, settings.CACHE_DASHBOARD_TIMEOUT)
        return JsonResponse(
            data={
                # товаров во всех магазинах сейчас:
                'totalValue': data['totalValue'],
                # объем всего рынка сегодня по сравнению со вчера:
                'valueDiff': data['valueDiff'],
                # топ категория за сегодня:
                'bestCatToday': data['bestCatToday'],
                # процент от общей суммы проданного для топ категории:
                'bestCatTodayPercent': data['bestCatTodayPercent'],
                # средняя цена сегодня за единицу товара:
                'averagePrice': data['averagePrice'],
                # на сколько изменилась средняя цена со вчера:
                'priceDiff': data['priceDiff'],
                # сумма продаж за текущий период в N-дней:
                'curDaysSumCost': data['curDaysSumCost'],
                # разница в продажах за предыдущий период в N-дней и текущий:
                'prevDaysSumDiff': data['prevDaysSumDiff'],
                # сумма продаж по категориями за N-дней:
                'totalDaysCatSum': data['totalDaysCatSum'],
                # продажи по категориям по дням:
                'days': data['days'],
                # статистика по магазам за сегодня(категории и значения):
                'shops': data['shops'],
            },
        )
    else:
        return HttpResponse("Only GET allowed")
