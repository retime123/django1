#coding=utf-8
from django.shortcuts import render
from models import *
from django.core.paginator import Paginator,Page
from df_cart.models import *

# Create your views here.
# 跳转到主页
def index(request):
    t1_click = GoodsInfo.objects.filter(gtype_id = 1).order_by('-gclick')[0:3]
    # 一对多  查询gtype_id为的所有数据,并以gclick为降序的列表
    t1_new = GoodsInfo.objects.filter(gtype_id = 1).order_by('-id')[0:4]
    t2_click = GoodsInfo.objects.filter(gtype_id=2).order_by('-gclick')[0:3]
    t2_new = GoodsInfo.objects.filter(gtype_id=2).order_by('-id')[0:4]
    t3_click = GoodsInfo.objects.filter(gtype_id=3).order_by('-gclick')[0:3]
    t3_new = GoodsInfo.objects.filter(gtype_id=3).order_by('-id')[0:4]
    t4_click = GoodsInfo.objects.filter(gtype_id=4).order_by('-gclick')[0:3]
    t4_new = GoodsInfo.objects.filter(gtype_id=4).order_by('-id')[0:4]
    t5_click = GoodsInfo.objects.filter(gtype_id=5).order_by('-gclick')[0:3]
    t5_new = GoodsInfo.objects.filter(gtype_id=5).order_by('-id')[0:4]
    t6_click = GoodsInfo.objects.filter(gtype_id=6).order_by('-gclick')[0:3]
    t6_new = GoodsInfo.objects.filter(gtype_id=6).order_by('-id')[0:4]

    context = {"title": "主页",
               'guest_cart': 1,
               't1_click': t1_click, 't1_new': t1_new,
               't2_click': t2_click, 't2_new': t2_new,
               't3_click': t3_click, 't3_new': t3_new,
               't4_click': t4_click, 't4_new': t4_new,
               't5_click': t5_click, 't5_new': t5_new,
               't6_click': t6_click, 't6_new': t6_new,
               'cart_count':cart_count(request),
               }
    return render(request, 'html/index.html', context)

def list(request,tid,tin,sort):
    typeinfo = TypeInfo.objects.get(pk=int(tid)) # get得到的是对象
    # print type(typeinfo)
    # 推荐商品
    news = GoodsInfo.objects.filter(gtype_id=int(tid)).order_by('-id')[0:2]# filter得到的是列表
    goods_list=[]
    if sort == '1': # 默认,最新
        goods_list = GoodsInfo.objects.filter(gtype_id=int(tid)).order_by('-id')
    elif sort == '2':# 价格
        goods_list = GoodsInfo.objects.filter(gtype_id=int(tid)).order_by('gprice')
    elif sort == '3':# 点击
        goods_list = GoodsInfo.objects.filter(gtype_id=int(tid)).order_by('-gclick')

    page1 = Paginator(goods_list,10)
    pages = page1.page(int(tin))

    context = {"title": typeinfo.title,
               # 'goods_list':goods_list,
               'typeinfo':typeinfo, #TypeInfo里面的种类id
               'sort':sort,# 排序
               'news':news,# 推荐商品
               'pages':pages,
               'cart_count': cart_count(request),
               }
    return render(request, 'html/list.html', context)


def detail(request,id):
    # print tid
    goods = GoodsInfo.objects.get(pk=int(id))# 对象
    goods.gclick = goods.gclick+1
    goods.save()

    tid = goods.gtype_id # 对应typeinfo里面的id号
    typeinfo = TypeInfo.objects.get(pk=int(tid))
    news = GoodsInfo.objects.filter(gtype_id=int(tid)).order_by('-id')[0:2]

    context = {"title": goods.gtitle,# 页面信息
               'typeinfo': typeinfo,
               'news': news,# 推荐商品
               'goods':goods,
               'cart_count': cart_count(request),
               }
    ret = render(request, 'html/detail.html', context)
    # 最近浏览
    liulan = request.COOKIES.get("liulan",'[]')# 字符串 读取cookie里的数据,没有数据--默认值''
    # 第一种
    # if liulan == '':
    #     ret.set_cookie('liulan',id)
    # else:
    #     liulan_list = liulan.split(',')#拆分字符串,成列表
    #     if id in liulan_list:# 去重
    #         liulan_list.remove(id)
    #     liulan_list.insert(0,id)#加到第一个
    #     if len(liulan_list)>5:
    #         liulan_list.pop()
    #     liulan2 = ','.join(liulan_list)
    #
    #     print liulan2
    #     ret.set_cookie('liulan',liulan2)

    # 第二种
    liulan_list = eval(liulan)
    if len(liulan_list) == 0:
        liulan_list.insert(0, id)
    else:
        if id in liulan_list:  # 去重
            liulan_list.remove(id)
        liulan_list.insert(0,id)#加到第一个
        if len(liulan_list) > 5:
            liulan_list.pop()
    liulan2 = str(liulan_list)
    ret.set_cookie('liulan', liulan2)
    return ret


def query(request):
    context = {'title':'搜索结果',
               }
    return render(request,'search/search.html', context)

def cart_count(request):# 中间函数,多次调用:用于显示购物车有多少商品
    # uid = request.session['user_id'] #没有登录,cookie里面没有'user_id'
    if request.session.has_key('user_id'):
        uid = request.session['user_id']
        return CartInfo.objects.filter(user_id = uid).count()
    else:
        return 0
