#coding=utf-8
from django.shortcuts import render
from models import *
from django.http import HttpResponse,JsonResponse
from hashlib import sha1
from df_user import user_de

# Create your views here.

@user_de.login
def cart(request):
    uid = request.session['user_id']
    context={"title":'购物车',
             'page_name': 1}

    return render(request,'html/cart.html',context)