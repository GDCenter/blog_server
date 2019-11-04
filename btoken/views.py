from django.shortcuts import render
from django.http import JsonResponse
import json
import time
import jwt
import hashlib
from  user.models import UserProfile
# from user.views import make_token
# Create your views here.

def btoken(request):
    if not request.method == 'POST':
        #创建token
        #当前视图函数只接受post

        result = {'code':101,'error':'Please use POST'}
        return JsonResponse(result)

    json_str = request.body
    if not json_str:
        # post 未提交数据

        result = {
            "code": "202",
            "error": "Please POST data"}

        return JsonResponse(result)

    json_obj = json.loads(json_str)
    username = json_obj.get("username")
    password = json_obj.get('password')
    if not username:
        result = {'code':103,'error':'Please give me username!'}
        return JsonResponse(result)
    if not password:
        result = {'code':104,'error':'Please give me pasword'}
        return JsonResponse(result)

    users= UserProfile.objects.filter(username=username)

    if not users:
        #当前用户不存在
        result={'code':105,'error':'The user is not existed'}
        return JsonResponse(result)

    #hash_password

    p_m = hashlib.sha1()
    p_m.update(password.encode())

    #对比密码:

    if p_m.hexdigest() != users[0].password:
        result = {'code':106,'error':'The username or password was worong'}
        return JsonResponse(result)

    token = make_token(username)
    result= {'code':200,'username':username,'data':{'token':token.decode()}}
    return JsonResponse(result)

def make_token(username, expire=3600 * 24):
        """
        生成token
        :param username:
        :param expire:
        :return:
        """
        key = "abcdef1234"
        now_t = time.time()
        payload = {
            "username": username,
            "exp": int(now_t + expire)
        }
        return jwt.encode(payload, key, algorithm="HS256")

