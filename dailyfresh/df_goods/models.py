#coding=utf-8
from django.db import models
from tinymce.models import HTMLField

# Create your models here.

class TypeInfo(models.Model):#商品种类
    title = models.CharField(max_length=40)
    IsDelete = models.BooleanField(default=False)
    def __str__(self):
        return self.title.encode('utf-8')


class GoodsInfo(models.Model):
    gtitle = models.CharField(max_length=20)
    gpic = models.ImageField(upload_to='goods')
    gprice = models.DecimalField(max_digits=5, decimal_places=2)
    isDelete = models.BooleanField(default=False)
    gunit = models.CharField(max_length=20, default='500g')
    gclick = models.IntegerField()
    gjianjie = models.CharField(max_length=200)
    gkucun = models.IntegerField()
    gcontent = HTMLField()
    gtype = models.ForeignKey(TypeInfo)# 一对多

    def __str__(self):
        return self.gtitle.encode('utf-8')
