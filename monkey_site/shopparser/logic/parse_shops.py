import requests
import re
import time
from django.utils import timezone
from django.core.cache import cache
from ..models import Shop, ShopState
from bs4 import BeautifulSoup as BS
from .cat_validator import catValidator
from .categories import getCatDict
from .update_stat import updateStat


def updateShopStats(pause):
    shopList = Shop.objects.all()
    # shopList = Shop.objects.filter(pk__lte=1)
    for shop in shopList:
        try:
            time.sleep(pause)
            cache.delete('dash_data')
            print(f'Очистил dash_cache. Магазин: {shop.url}')
            CatDict = getCatDict()
            pageData = BS(requests.get(shop).text, 'lxml')
            # pageData = BS(open("sample.txt").read(), 'lxml')

            for catID in [cat.get('data-catid') for cat in pageData.find_all('tr', {'class': 'showgoods_cat'})]:
                catName = pageData.find('tr', {'data-catid': catID}).text
                definedCat = catValidator(catName)
                catItemsCount = 0
                catItemsPrice = 0
                for good_item in pageData.find_all('tr', {'class': f'goods by_cat_id_{catID}'}):
                    count = good_item.find('td', {'class': 'td-count'}).text
                    price = re.search(
                        r'>([\d.]+) Руб.', str(good_item.find('td', {'class': 'td-price'}))).group(1)
                    itemsPrice = int(int(count)*float(price))
                    catItemsCount += int(count) 
                    catItemsPrice += itemsPrice
                CatDict[definedCat] = [CatDict[definedCat][0] +
                                       catItemsCount, CatDict[definedCat][1] + catItemsPrice]
            # в этот блок кода надо передать объект магазина и словарь состояний по всем полям (CatDict)
            updateStat(shop, CatDict)
        except:
            print('Сайт недоступен')
