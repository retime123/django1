#coding=utf-8
from django.shortcuts import render
from models import *
from django.http import HttpResponse,JsonResponse
from hashlib import sha1
from df_user import user_login

# Create your views here.

@user_login.login
def myorder(request):
    uid = request.session['user_id']
    context = {"title": '订单',
               'page_name': 1}

    return render(request, 'html/place_order.html', context)