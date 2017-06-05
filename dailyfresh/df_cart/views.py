#coding=utf-8
from django.shortcuts import render,redirect
from models import *
from django.http import HttpResponse,JsonResponse

from df_user import user_login

# Create your views here.

@user_login.login
def cart_list(request):
    uid = request.session['user_id']
    cart_list = CartInfo.objects.filter(user_id=uid)
    print cart_list
    context={"title":'购物车',
             'page_name': 1,
             'carts': cart_list,
             }
    return render(request,'html/cart.html',context)

@user_login.login
def add(request,gid,count):
    uid = request.session['user_id']
    # 当前用户,商品id编号的所有信息
    carts = CartInfo.objects.filter(goods_id = gid).filter(user_id = uid)
    if len(carts)== 0:
        cart = CartInfo()
        cart.goods_id = int(gid)
        cart.user_id = uid
        cart.count = int(count)
        cart.save()
    else:
        cart = carts[0]
        cart.count += int(count)
        cart.save()
    if request.is_ajax():
        return JsonResponse({'count': CartInfo.objects.filter(user_id=uid).count()})
    else:
        return redirect('/cart/')

