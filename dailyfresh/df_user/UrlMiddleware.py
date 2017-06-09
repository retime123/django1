#coding=utf-8
from django.http import HttpRequest,HttpResponse
from django.middleware.csrf import CsrfViewMiddleware
class url():#中间件
    def process_response(self, request, response):
        url_list=[
            '/user/register.html/',
            '/user/register_handle/',
            '/user/register_exist/',
            '/user/login.html',
            '/user/login_handle/',
            '/user/logout/'
        ]

        if not request.is_ajax() and request.path not in url_list:

            response.set_cookie('red_url',request.get_full_path())
        return response
