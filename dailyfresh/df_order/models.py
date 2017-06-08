#coding=utf-8
from django.db import models

# Create your models here.
class OrderInfo(models.Model):# 主表
    oid= models.CharField(max_length=20,primary_key=True)
    user = models.ForeignKey('df_user.FreshInfo')#关联:一对多,生成表是user_id
    isPay = models.BooleanField(default=False)
    odate = models.DateTimeField(auto_now_add=True)
    ototal = models.DecimalField(max_digits=7,decimal_places=2)#这个订单总金额:5+2小数
    oaddress = models.CharField(max_length=150)


class OrderDetailInfo(models.Model):
    goods = models.ForeignKey('df_goods.GoodsInfo')
    order = models.ForeignKey(OrderInfo)
    price = models.DecimalField(max_digits=5,decimal_places=2)#单价
    count = models.IntegerField()