#coding=utf-8
from django.shortcuts import render
from models import *
from django.http import HttpResponse,JsonResponse
from hashlib import sha1
# Create your views here.
def myorder(request):
    context = {"title": '订单',
               'page_name': 1}

    return render(request, 'html/detail.html', context)