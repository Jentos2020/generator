from __future__ import absolute_import, unicode_literals
from celery import shared_task
from celery.schedules import crontab
from .logic.yesterday_info import updateYesterdayInfo
from .logic.parse_shops import updateShopStats
from monkey_site.celery import app
import random


@shared_task
def taskUpadteDB():
    # print('Parsing starts')
    pause = random.uniform(30, 40)
    updateShopStats(pause)


@shared_task
def taskYesterdayStat():
    updateYesterdayInfo()


app.conf.beat_schedule = {
    'parsing_shops': {
        'task': 'shopparser.tasks.taskUpadteDB',
        'schedule': crontab(minute=0, hour='0, 6, 15, 21'),
        'options': {
            'retry': False,
            'expires': 60*60*24,
            },
    },
    'yest_stat': {
        'task': 'shopparser.tasks.taskYesterdayStat',
        'schedule': crontab(minute=55, hour=23),
        'options': {
            'retry': False,
            'expires': 60*60*24*2,
            },
    },
}
