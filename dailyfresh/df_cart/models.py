#coding=utf-8
from django.db import models

# Create your models here.
class CarInfo(models.Model):
    user = models.ForeignKey('df_user.FreshInfo')
    goods = models.ForeignKey('df_goods.GoodsInfo')
    count = models.IntegerField()