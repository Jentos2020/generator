from datetime import datetime
from rest_framework import serializers
from .models import DayStat, ShopState, Shop


class DayStatSerializer(serializers.Serializer):
    day = serializers.DateTimeField()
    BM_count = serializers.IntegerField()
    BM_cost = serializers.IntegerField()
    ZRD_count = serializers.IntegerField()
    ZRD_cost = serializers.IntegerField()
    Farm_count = serializers.IntegerField()
    Farm_cost = serializers.IntegerField()
    Autoreg_count = serializers.IntegerField()
    Autoreg_cost = serializers.IntegerField()
    FP_count = serializers.IntegerField()
    FP_cost = serializers.IntegerField()
    PZRDFP_count = serializers.IntegerField()
    PZRDFP_cost = serializers.IntegerField()
    Undef_count = serializers.IntegerField()
    Undef_cost = serializers.IntegerField()

    def to_representation(self, instance):
        newDateFormat = super().to_representation(instance)
        newDateFormat['day'] = newDateFormat['day'][:10]
        return newDateFormat
    
    
    
class DaysSumSerializer(serializers.ModelSerializer):
    class Meta:
        model = DayStat
        exclude = 'shop', 'time_update'
    

class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        exclude = 'id',


class ShopStatSerializer(serializers.ModelSerializer):
    shop = ShopSerializer()
    class Meta:
        model = ShopState
        exclude = 'id', 'time_update', 
        
