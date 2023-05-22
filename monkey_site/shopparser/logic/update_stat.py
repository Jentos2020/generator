from django.utils import timezone
from ..models import ShopState, DayStat


def updateStat(shop, CatDict):
    # велась ли уже статистика по этому магазу, если нет, добавляем запись
    if ShopState.objects.filter(shop_id=shop.pk).exists():
        # статистика ведется, будем сравнивать записи прошлой проверки с данными текущей проверки(CatDict)
        oldState = ShopState.objects.get(shop_id=shop.pk)
        # старые данные по этому магазину
        oldData = [
            oldState.BM_count,
            oldState.BM_cost,
            oldState.ZRD_count,
            oldState.ZRD_cost,
            oldState.Farm_count,
            oldState.Farm_cost,
            oldState.Autoreg_count,
            oldState.Autoreg_cost,
            oldState.FP_count,
            oldState.FP_cost,
            oldState.PZRDFP_count,
            oldState.PZRDFP_cost,
            oldState.Undef_count,
            oldState.Undef_cost,
        ]
        # print(f'Старые данные: {oldData}')
        # новые данные по этому магазину
        newData = [
            CatDict['БМ'][0],
            CatDict['БМ'][1],
            CatDict['ПЗРД'][0],
            CatDict['ПЗРД'][1],
            CatDict['Фарм'][0],
            CatDict['Фарм'][1],
            CatDict['Авторег'][0],
            CatDict['Авторег'][1],
            CatDict['ФП'][0],
            CatDict['ФП'][1],
            CatDict['ФП ПЗРД'][0],
            CatDict['ФП ПЗРД'][1],
            CatDict['Undefined'][0],
            CatDict['Undefined'][1],
        ]
        print(f'Новые данные:  {newData}')
        # сюда запишем данные о доходе и продажах
        dayData = [
            ['shop', shop.pk],
            ['BM_count', 0],
            ['BM_cost', 0],
            ['ZRD_count', 0],
            ['ZRD_cost', 0],
            ['Farm_count', 0],
            ['Farm_cost', 0],
            ['Autoreg_count', 0],
            ['Autoreg_cost', 0],
            ['FP_count', 0],
            ['FP_cost', 0],
            ['PZRDFP_count', 0],
            ['PZRDFP_cost', 0],
            ['Undef_count', 0],
            ['Undef_cost', 0],
        ]
        # проверяем старые и новые данные, если есть продажи/доход, записываем в dayData
        for index, oldItems in enumerate(oldData):
            diff = oldItems - newData[index]
            if (diff) > 0:
                dayData[index + 1][1] = diff
        # ^ diff - продажи/доход, oldItems - было, newData[index] - стало
        # list => dict, чтобы потом можно было сохранить в модель DayStat
        dayDataDict = {key[0]: key[1] for key in dayData}
        dayDataDict['shop'] = shop
        print(f'Изменения полей с прошлого раза: {list(dayDataDict.values())}')
        # если запись по этому магазу уже есть за сегодня, то суммируем значения полей которые уже были
        # с новыми значениями, т.е. модифицируем имеющуюся запись, если за сегодня нет этого магаза, создаем запись
        if DayStat.objects.filter(shop_id=shop.pk, time_update__date=timezone.now().date()).exists():
            print('За сегодня уже есть запись по магазину, добавляем к ней значения')
            currentShopDayStat = DayStat.objects.get(
                shop_id=shop.pk, time_update__date=timezone.now().date())
            currentShopDayStat.BM_count = (currentShopDayStat.BM_count + dayDataDict['BM_count'])
            currentShopDayStat.BM_cost = (currentShopDayStat.BM_cost + dayDataDict['BM_cost'])
            currentShopDayStat.ZRD_count = (currentShopDayStat.ZRD_count + dayDataDict['ZRD_count'])
            currentShopDayStat.ZRD_cost = (currentShopDayStat.ZRD_cost + dayDataDict['ZRD_cost'])
            currentShopDayStat.Farm_count = (currentShopDayStat.Farm_count + dayDataDict['Farm_count'])
            currentShopDayStat.Farm_cost = (currentShopDayStat.Farm_cost + dayDataDict['Farm_cost'])
            currentShopDayStat.Autoreg_count = (currentShopDayStat.Autoreg_count + dayDataDict['Autoreg_count'])
            currentShopDayStat.Autoreg_cost = (currentShopDayStat.Autoreg_cost + dayDataDict['Autoreg_cost'])
            currentShopDayStat.FP_count = (currentShopDayStat.FP_count + dayDataDict['FP_count'])
            currentShopDayStat.FP_cost = (currentShopDayStat.FP_cost + dayDataDict['FP_cost'])
            currentShopDayStat.PZRDFP_count = (currentShopDayStat.PZRDFP_count + dayDataDict['PZRDFP_count'])
            currentShopDayStat.PZRDFP_cost = (currentShopDayStat.PZRDFP_cost + dayDataDict['PZRDFP_cost'])
            currentShopDayStat.Undef_count = (currentShopDayStat.Undef_count + dayDataDict['Undef_count'])
            currentShopDayStat.Undef_cost = (currentShopDayStat.Undef_cost + dayDataDict['Undef_cost'])
            currentShopDayStat.save()
        else:
            print('По этому магазу сегодня еще не было записи')
            DayStat(**dayDataDict).save()
        # запомниаем это состояние магазина для следующего раза
        oldState.BM_count = CatDict['БМ'][0]
        oldState.BM_cost = CatDict['БМ'][1]
        oldState.ZRD_count = CatDict['ПЗРД'][0]
        oldState.ZRD_cost = CatDict['ПЗРД'][1]
        oldState.Farm_count = CatDict['Фарм'][0]
        oldState.Farm_cost = CatDict['Фарм'][1]
        oldState.Autoreg_count = CatDict['Авторег'][0]
        oldState.Autoreg_cost = CatDict['Авторег'][1]
        oldState.FP_count = CatDict['ФП'][0]
        oldState.FP_cost = CatDict['ФП'][1]
        oldState.PZRDFP_count = CatDict['ФП ПЗРД'][0]
        oldState.PZRDFP_cost = CatDict['ФП ПЗРД'][1]
        oldState.Undef_count = CatDict['Undefined'][0]
        oldState.Undef_cost = CatDict['Undefined'][1]
        oldState.save()
    else:
        print('Такой магаз еще не начали отслеживать, добавляем')
        ShopState(
            shop=shop,
            BM_count=CatDict['БМ'][0],
            BM_cost=CatDict['БМ'][1],
            ZRD_count=CatDict['ПЗРД'][0],
            ZRD_cost=CatDict['ПЗРД'][1],
            Farm_count=CatDict['Фарм'][0],
            Farm_cost=CatDict['Фарм'][1],
            Autoreg_count=CatDict['Авторег'][0],
            Autoreg_cost=CatDict['Авторег'][1],
            FP_count=CatDict['ФП'][0],
            FP_cost=CatDict['ФП'][1],
            PZRDFP_count=CatDict['ФП ПЗРД'][0],
            PZRDFP_cost=CatDict['ФП ПЗРД'][1],
            Undef_count=CatDict['Undefined'][0],
            Undef_cost=CatDict['Undefined'][1],
        ).save()
