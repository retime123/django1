#coding=utf-8
from django.shortcuts import render,redirect
from models import *
from django.http import HttpResponse,JsonResponse
from django.http import HttpResponseRedirect
from hashlib import sha1
from . import user_de

# Create your views here.
# 跳转到主页
def index(request):
    context = {"title":"主页",
               'guest_cart': 1,}
    return render(request,'html/index.html',context)

# 跳转到注册页面
def register(request):
    context = {"title": "注册"}
    return render(request,'html/register.html',context)

# 获取表单提交的内容
def register_post(request):
    # print '2222'
    dict = request.POST
    fname = dict.get('user_name')
    fpwd1 = dict.get('pwd')
    fpwd2 = dict.get('cpwd')
    a = sha1()
    a.update(fpwd2)
    fpwd3 = a.hexdigest()
    femail = dict.get('email')
    data = FreshInfo.objects.create(fname=fname,fpwd=fpwd3,femail=femail)
    data.save()
    # 注册成功 回登陆页面
    return render(request,'html/login.html')

# 获取名字是否重复
def register_exist(request):
    # 获取名字
    uname = request.GET.get('name')
    # uname = request.POST.get('user_name')
    count = FreshInfo.objects.filter(fname=uname).count()
    # print count
    return JsonResponse({'count': count})

# 跳转到登陆页面
def login(request):
    uname = request.COOKIES.get('uname', '')
    context = {'title': '用户登录', 'error_name': 0, 'error_pwd': 0, 'uname': uname}
    return render(request,'html/login.html',context)

#
def login_handle(request):
    # 获取提交表单的内容
    post=request.POST
    uname=post.get('username')
    print uname
    upwd=post.get('pwd')
    jizhu=post.get('jizhu',0)
    # 根据用户名查询对象 获得列表 列表里面是字典
    users=FreshInfo.objects.filter(fname=uname)#[{}]
    # print users
    # 判断是否查到用户名,如果查到则判断密码是否正确,正确则转到用户中心
    if len(users) == 1:
        s1 = sha1()
        s1.update(upwd)
        if s1.hexdigest() == users[0].fpwd:
            url = request.COOKIES.get('url', '/')
            red = HttpResponseRedirect(url)
            # 成功后删除转向地址,防止以后直接登录造成的转向
            red.set_cookie('url', '', max_age=-1)
            # 记住用户名
            if jizhu != 0:
                red.set_cookie('uname', uname)
            else:
                red.set_cookie('uname', '', max_age=-1)
            request.session['user_id'] = users[0].id
            request.session['user_name'] = uname
            return red
        else:
            context = {'title': '用户登录', 'error_name': 0, 'error_pwd': 1, 'uname': uname, 'upwd': upwd}
            return render(request, 'html/login.html', context)
    else:
        context = {'title': '用户登录', 'error_name': 1, 'error_pwd': 0, 'uname': uname, 'upwd': upwd}
        return render(request, 'html/login.html', context)

def logout(request):
    request.session.flush()# flush()清除
    return redirect('/')

@user_de.login
def info(request):# 用户中心
    # 判断是否登陆,未登录则跳转到登录页面!
    # 用装饰器
    # if request.session.has_key('user_id'):
    #     return func(request, *args, **kwargs)
    # else:
    #     red = HttpResponseRedirect('/login.html/')
    #     red.set_cookie('url', request.get_full_path())
    #     return red

    user_email = FreshInfo.objects.get(id=request.session['user_id']).femail
    # 最近浏览
    goods_list = []
    goods_ids = request.COOKIES.get('goods_ids', '')
    if goods_ids != '':
        goods_ids1 = goods_ids.split(',')  # ['']
        # GoodsInfo.objects.filter(id__in=goods_ids1)
        for goods_id in goods_ids1:
            goods_list.append(GoodsInfo.objects.get(id=int(goods_id)))

    context = {'title': '用户中心',
               'user_name': request.session['user_name'],
               'user_email': user_email,
               'page_name': 1,
               'goods_list': goods_list,
                "info_active":'active',
               }

    return render(request, 'html/user_center_info.html',context)

@user_de.login
def order(request):# 订单
    context = {"title": "用户中心",
                'page_name': 1,
               "order_active":'active',
               }
    return render(request, 'html/user_center_order.html', context)

@user_de.login
def site(request):
    user = FreshInfo.objects.get(id=request.session['user_id'])
    if request.method == 'POST':
        post = request.POST
        user.frecipients = post.get('ushou')# 收件人
        user.faddress = post.get('uaddress')
        user.fyoubian = post.get('uyoubian')
        user.fphone = post.get('uphone')
        user.save()
    context = {'title': '用户中心',
               'user': user,
               'page_name': 1,
               "site_active":'active',
               }
    return render(request, 'html/user_center_site.html', context)