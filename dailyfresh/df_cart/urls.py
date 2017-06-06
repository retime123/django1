# coding=utf-8
from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$',views.cart_list),
    url(r'^add(\d+)_(\d+)/?$',views.add),
    url(r'^get/?$',views.cart_count),
    url(r'^delete/?$',views.cart_delete),

]