from __future__ import absolute_import, unicode_literals
from time import sleep
from celery import shared_task
from monkey_site.celery import app
import os
import base64
from .creation.new_image import docMaking


@shared_task
def delImg(imgName):
    print('Приступаю к удалению картинки')
    sleep(5)
    if os.path.exists(imgName):
        os.remove(imgName)
        print(f"Файл {imgName} успешно удален")
    else:
        print(f"Файл {imgName} не найден, не смог удалить.")


@shared_task
def makeImg(data):
    sleep(1)
    photo = docMaking(data)
    delImg.apply_async(args=[photo])
    print(f'Создал картинку, путь: {photo}')
    with open(photo, "rb") as img:
        encoded = base64.b64encode(img.read()).decode("utf-8")
    return encoded


app.conf.beat_schedule = {
    'makeImg': {
        'task': 'shopparser.tasks.makeImg',
        'options': {
            'retry': False,
            'expires': 60*5,
        },
    },
    'delImg': {
        'task': 'shopparser.tasks.delImg',
        'options': {
            'retry': False,
            'expires': 60,
        },
    },
}
