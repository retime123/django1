# coding=utf-8
from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$|index/?$', views.index),

    url((r'^list(\d+)_(\d+)_(\d+)/?$'),views.list),# 列表
    url((r'^detail(\d+)/?$'),views.detail), # 商品详细
    # url((r'^search/'),views.mysearch),
    url(r'^query/', views.query),
]