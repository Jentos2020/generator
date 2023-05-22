from ..models import ShopState
from django.core.cache import cache
from django.db.models import Sum
from django.db.models import F


def allValue():
    # подсчет объема всех товаров
    products = ShopState.objects.aggregate(
        total_value=Sum(
            F('BM_cost') + F('ZRD_cost') + F('Farm_cost') + F('Autoreg_cost') + F('FP_cost') + F('PZRDFP_cost'))
    )
    return products['total_value']


def updateYesterdayInfo():
    print('Записываю данные за сегодняшний день')
    cache.set('yest_value', allValue(), 60*60*25)
    curPrice = cache.get('cur_price')
    if not curPrice:
        curPrice = 1
    cache.set('yest_price', curPrice, 60*60*25)

