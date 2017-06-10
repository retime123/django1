#coding=utf-8
from django.shortcuts import render,redirect
from models import *
from django.http import HttpResponse,JsonResponse
from df_user import user_login
from df_user.models import *
from df_cart.models import *
from django.db import transaction
from datetime import datetime
# Create your views here.

@user_login.login
def myorder(request):
    uid = request.session['user_id']
    user = FreshInfo.objects.get(id=uid)
    cart_id = request.GET.getlist('cart_id')
    # carts = CartInfo.objects.filter(id__in=cart_id)[::-1]
    carts = CartInfo.objects.filter(id__in=cart_id).order_by('-id')
    context = {"title": '订单',
               'page_name': 1,
               'user':user,
                'carts':carts,
               }
    return render(request, 'html/place_order.html', context)

@transaction.atomic
def order_handle(request):# 订单数据处理
    post = request.POST
    cart_id = post.getlist('cart_id')
    address = post.get('address')
    #print address
    sid = transaction.savepoint()# Django里面的事务委托
    try:
        order = OrderInfo()
        nowtime = datetime.now()
        uid = request.session['user_id']
        order.oid = '%s%d' %(nowtime.strftime('%Y%m%d%H%M%S'),uid)
        #print order.oid
        order.user_id = uid
        order.odate = nowtime
        order.oaddress = address
        order.ototal =0
        order.save()

        total = 0
        for cid in cart_id:
            cart = CartInfo.objects.get(pk=cid)
            if cart.goods.gkucun >= cart.count:#库存
                # 库存足够,可以购买:库存减少
                cart.goods.gkucun -= cart.count
                cart.goods.save()
                #将信息加入详单
                detail = OrderDetailInfo()
                detail.order = order
                detail.goods = cart.goods
                detail.price = cart.goods.gprice
                detail.count = cart.count
                detail.save()
                total += cart.goods.gprice * cart.count
                # 删除购物车数据
                cart.delete()
            else:
                #库存不够
                transaction.savepoint_rollback(sid)#回滚：数据回到当初那样
                return redirect('/cart/')

        order.ototal = total
        order.save()
        transaction.savepoint_commit(sid)# 数据没问题，保存
        return redirect('/user/order1/')

    except Exception, e:
        # print e
        transaction.savepoint_rollback(sid)
        return redirect('/cart/')

# def instantly(request):
#     uid = request.session['user_id']
#     goods_id = request.GET.get('goods_id')
#     count = request.GET.get('count')


