from .categories import Categories

catList = Categories()[0]
catPZRDFP = Categories()[1]


def catValidator(title):
    title = title.lower()
    catReturn = 'Undefined'
    for (index, cat) in enumerate(catList):
        catFound = (any(key in title for key in catList[index][1]) and not any(
            stopKey in title for stopKey in catList[index][2]))
        if catFound:
            catReturn = cat[0] 
            break

    # отдельная проверка для ФП ПЗРД
    if not catReturn:
        catFound = (any(key in title for key in catPZRDFP[1]) and any(
            key in title for key in catPZRDFP[2]) and not any(stopKey in title for stopKey in catPZRDFP[3]))
        if catFound:
            catReturn = catPZRDFP[0]
    return catReturn