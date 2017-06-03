#coding=utf-8
from django.db import models

# Create your models here.

class TypeGoods(models.Model):#商品种类
    title = models.CharField(max_length=40)


class GoodsInfo(models.Model):
    pass