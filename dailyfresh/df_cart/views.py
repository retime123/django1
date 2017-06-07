#coding=utf-8
from django.shortcuts import render,redirect
from models import *
from django.http import HttpResponse,JsonResponse

from df_user import user_login

# Create your views here.

@user_login.login
def cart_list(request):
    uid = request.session['user_id']
    cart_list = CartInfo.objects.filter(user_id=uid)[::-1]#反序
    # print cart_list

    context={"title":'购物车',
             'page_name': 1,
             'carts': cart_list,
             }
    return render(request,'html/cart.html',context)

@user_login.login
def add(request,gid,count):# 商品添加
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
        # 判断新添加的数量有没有超过 库存
        if cart.count < cart.goods.gkucun:
            cart.count += int(count)
            cart.save()
    if request.is_ajax():
        return JsonResponse({'count': CartInfo.objects.filter(user_id=uid).count()})
    else:
        return redirect('/cart/')

@user_login.login
def cart_count(request):# 购物车页
    uid = request.session['user_id']
    goods = request.GET.get('goods')
    count = request.GET.get('count')
    print count
    cart = CartInfo.objects.filter(goods_id = goods).filter(user_id = uid)[0]
    cart.count = int(count)
    cart.save()
    return JsonResponse({'count': 'ok'})

@user_login.login
def cart_delete(request):# 删除
    uid = request.session['user_id']
    cart_id = request.GET.get('cart_id')
    cart = CartInfo.objects.filter(id = cart_id)
    cart.delete()
    return  JsonResponse({'delete': 'ok'})


