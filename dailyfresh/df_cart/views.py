#coding=utf-8
from django.shortcuts import render,redirect
from models import *
from django.http import HttpResponse,JsonResponse

from df_user import user_de

# Create your views here.

@user_de.login
def cart(request):
    uid = request.session['user_id']
    carts = CarInfo.objects.filter(user_id=uid)
    context={"title":'购物车',
             'page_name': 1}

    return render(request,'html/cart.html',context)




