#coding=utf-8
from django.shortcuts import render
from models import *
from django.core.paginator import Paginator,Page


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
               }
    return render(request, 'html/index.html', context)

def list(request,tid,tin,sort):
    type = TypeInfo.objects.get(pk=int(tid)) # get得到的是对象
    title = type.title
    # print type(typeinfo)
    # 推荐商品
    news = GoodsInfo.objects.filter(gtype_id=int(tid)).order_by('-id')[0:2]# filter得到的是列表
    # goods_list=[]
    if sort == '1': # 默认,最新
        goods_list = GoodsInfo.objects.filter(gtype_id=int(tid)).order_by('-id')
    elif sort == '2':# 价格
        goods_list = GoodsInfo.objects.filter(gtype_id=int(tid)).order_by('gprice')
    elif sort == '3':# 点击
        goods_list = GoodsInfo.objects.filter(gtype_id=int(tid)).order_by('-gclick')

    page1 = Paginator(goods_list,10)
    pages = page1.page(int(tin))

    context = {"title": title,
               't_title': title,
               # 'goods_list':goods_list,
               'typeinfo':tid, #TypeInfo里面的种类id
               'sort':sort,# 排序
               'news':news,# 推荐商品
               'pages':pages,
               }
    return render(request, 'html/list.html', context)


def detail(request,id):
    # print tid
    type = GoodsInfo.objects.get(pk=int(id))# 对象
    tid = type.gtype_id # typeinfo里面的id号

    title = TypeInfo.objects.get(pk=int(tid))

    news = GoodsInfo.objects.filter(gtype_id=int(tid)).order_by('-id')[0:2]
    # news = GoodsInfo.gtype.goodsinfo_set.order_by('-id')[0:2]
    context = {"title": type.gtitle,# 页面信息
               't_title':title,
               'typeinfo': tid,
               'news': news,# 推荐商品
               'goods':type,
               }
    return render(request, 'html/detail.html', context)

def mysearch(request):
    context = {"title": '搜索',  # 页面信息

               }
    return render(request, 'search/search.html', context)

def query(request):
    context = {'title':'搜索结果',
               }
    return render(request,'search/search.html', context)
    # pass