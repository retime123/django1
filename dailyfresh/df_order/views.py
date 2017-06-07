#coding=utf-8
from django.shortcuts import render
from models import *
from django.http import HttpResponse,JsonResponse
from hashlib import sha1
from df_user import user_login
from df_user.models import *
from df_cart.models import *
# Create your views here.

@user_login.login
def myorder(request):
    uid = request.session['user_id']
    user = FreshInfo.objects.get(id=uid)
    cart_id = request.GET.getlist('cart_id')
    carts = CartInfo.objects.filter(id__in=cart_id)[::-1]
    context = {"title": '订单',
               'page_name': 1,
               'user':user,
                'carts':carts,
               }
    return render(request, 'html/place_order.html', context)

def order_handle(request):
    post = request.GET
    pass