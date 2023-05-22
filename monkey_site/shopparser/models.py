from django.db import models

# Create your models here.


class Shop(models.Model):
    url = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.url

# парсер сравнивает полученные значения с теми что будут здесь и в зависимости
# от результата записывает данные о прибыли или о кол-ве продаж товара в DayStat
class ShopState(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.PROTECT)
    time_update = models.DateTimeField(auto_now_add=True)
    BM_count = models.BigIntegerField()
    BM_cost = models.BigIntegerField()
    ZRD_count = models.BigIntegerField()
    ZRD_cost = models.BigIntegerField()
    Farm_count = models.BigIntegerField()
    Farm_cost = models.BigIntegerField()
    Autoreg_count = models.BigIntegerField()
    Autoreg_cost = models.BigIntegerField()
    FP_count = models.BigIntegerField()
    FP_cost = models.BigIntegerField()
    PZRDFP_count = models.BigIntegerField()
    PZRDFP_cost = models.BigIntegerField()
    Undef_count = models.BigIntegerField()
    Undef_cost = models.BigIntegerField()
    

# аккумулирует данные по каждому магазину за сутки и раз в день(в конце дня),
# передает обобщенные данные(без разбиения по магазинам) в MarketState
class DayStat(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.PROTECT)
    time_update = models.DateTimeField(auto_now_add=True)
    BM_count = models.BigIntegerField()
    BM_cost = models.BigIntegerField()
    ZRD_count = models.BigIntegerField()
    ZRD_cost = models.BigIntegerField()
    Farm_count = models.BigIntegerField()
    Farm_cost = models.BigIntegerField()
    Autoreg_count = models.BigIntegerField()
    Autoreg_cost = models.BigIntegerField()
    FP_count = models.BigIntegerField()
    FP_cost = models.BigIntegerField()
    PZRDFP_count = models.BigIntegerField()
    PZRDFP_cost = models.BigIntegerField()
    Undef_count = models.BigIntegerField()
    Undef_cost = models.BigIntegerField()


# содержит и выводит обобщенные данные по продажам за сутки по различным категориям
class MarketState(models.Model):
    time_update = models.DateTimeField(auto_now_add=True)
    BM_count = models.BigIntegerField()
    BM_cost = models.BigIntegerField()
    ZRD_count = models.BigIntegerField()
    ZRD_cost = models.BigIntegerField()
    Farm_count = models.BigIntegerField()
    Farm_cost = models.BigIntegerField()
    Autoreg_count = models.BigIntegerField()
    Autoreg_cost = models.BigIntegerField()
    FP_count = models.BigIntegerField()
    FP_cost = models.BigIntegerField()
    PZRDFP_count = models.BigIntegerField()
    PZRDFP_cost = models.BigIntegerField()
    Undef_count = models.BigIntegerField()
    Undef_cost = models.BigIntegerField()
