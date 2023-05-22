import requests
import os
import re
import random
from django.conf import settings
from django.http import HttpResponse
from datetime import datetime
from time import sleep


def faceDownload(url):
    currTime = datetime.now()
    fileName = currTime.strftime('%Y-%m-%d-%H-%M-%S')
    imgName = ''
    try:
        response = requests.get(url)
        if response.status_code == 200:
            pageData = response.text
            regex = r'<img src="([^"]+)" class="img-responsive"'
            match = re.search(regex, pageData)
            sleep(1)
            imgUrl = match.group(1)
            imgResp = requests.get(url + imgUrl)
            savePath = os.path.join(settings.MEDIA_ROOT, 'docs/new_faces')
            os.makedirs(savePath, exist_ok=True)
            imgName = os.path.join(savePath, f'{fileName}.jpg')
            img = imgResp.content
            with open(imgName, 'wb') as file:
                file.write(img)
        else:
            print('Сайт не открылся')
    except:
        print('Не удалось сгенерировать изображение, беру из базы')
        imgName = randImgSelect('random_faces')
    return imgName


def randImgSelect(folder: str):
    folderPath = os.path.join(settings.MEDIA_ROOT, 'docs', folder)
    collection = os.listdir(folderPath)
    fileName = random.choice(collection)
    return fileName if folder == 'random_faces' else os.path.join(settings.MEDIA_ROOT, 'docs', folder, fileName)
