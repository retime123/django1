#coding=utf-8
from django.shortcuts import render,redirect
from models import *
from django.http import HttpResponse,JsonResponse

from df_user import user_de

# Create your views here.

@user_de.login
def cart(request):
    uid = request.session['user_id']
    carts = CartInfo.objects.filter(user_id=18)
    print carts
    context={"title":'购物车',
             'page_name': 1,
             'carts': carts,
             }
    return render(request,'html/cart.html',context)

@user_de.login
def add(request):
    uid = request.session['user_id']


    return redirect('/cart/')