from .logic import categories


keys = ['БМ', 'Авторег', 'ПЗРД', 'БМ', 'ФП', ]
count = [5, 2, 2, 6, 4, ]
price = [500, 200, 200, 600, 400, ]


def getCatDict():
    CatDict = dict()
    category = categories.Categories()
    
    # цикл заполняет словарь категориями и дефолтными значениями,
    # затем хардкодим добавление второй категории с нестандартной структурой
    CatDict = {key[0]: [0, 0] for key in category[0]}
    CatDict[category[1][0]] = [0, 0]
    
    # заполняем словарь значениями(количество, стоимость), сопоставляя 
    # полученные ключи(категории) и теми, что есть в базе, если ключ 
    # повторяется значение не перезаписывается, а прибавляется к прошлому
    for index, key in enumerate(keys):
        CatDict[key] = [CatDict[key][0] + count[index], CatDict[key][1] + price[index]]
    