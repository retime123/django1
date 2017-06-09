#coding=utf-8
from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.myorder),
    url(r'^order_handle/?$', views.order_handle),
    url(r'^instantly/?$',views.instantly)
]