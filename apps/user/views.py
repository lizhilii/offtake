import re

from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.urls import reverse
from django.conf import settings
from django.core.mail import send_mail
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import SignatureExpired
from .models import User

def error_response(message):
    content = {}
    content['status'] = 'ERROR'
    content['error_message'] = message
    return JsonResponse(content)

def send_email(user_name, user_token_id, email):
    # 发送激活邮件
    subject = '激活邮件'
    html = '<h3>%s欢迎你使用本平台</h3><br/>激活链接<a href="http://127.0.0.1:8000/user/user_active/%s">http://127.0.0.1:8000/user/user_active/%s</a>'%(user_name, user_token_id, user_token_id)
    send_mail(subject, '', settings.EMAIL_HOST_USER, [email], html_message=html)


def register(request):

    if request.method == 'GET':
        return render(request, 'register.html')

    else:
        # 接收数据
        user_name = request.POST.get('user_name')
        pwd = request.POST.get('pwd')
        cpwd = request.POST.get('cpwd')
        email = request.POST.get('email')

        # 校验数据
        if(len(user_name) < 5 or len(user_name) > 20):
            return error_response('user_name')
        if(len(pwd) < 8 or len(pwd) > 20):
            return error_response('pwd')
        if(pwd != cpwd):
            return error_response('cpwd')
        if(re.match(r'^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$', email) == None):
            return error_response('email')
        if(User.objects.filter(username=user_name).exists()):
            return error_response('user_name_exists')

        # 数据处理
        user = User()
        user.username = user_name
        user.set_password(pwd)
        user.email=email
        user.is_active = False
        user.save()
        # 发送激活邮件

        content = {}
        content['status'] = 'SUCCESS'
        content['url'] = reverse('goods:index')

        # 对用户信息进行加密
        user_token_id = user.generate_activate_token()
        # 发送激活邮件
        send_email(user_name, user_token_id, email)

        return JsonResponse(content)

def user_active(request, token):
    serializer = Serializer(settings.SECRET_KEY, 3600)
    try:
        info = serializer.loads(token)

    except SignatureExpired as e:
        return HttpResponse('激活已经过期')
    else:
        user_id = info['confirm']
        user = User.objects.get(id=user_id)
        if(user != ''):
            user.is_active = True
            user.save()
            return HttpResponse('用户已激活')
        else:
            return HttpResponse('用户不存在')