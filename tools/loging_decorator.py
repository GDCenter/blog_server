import jwt
KEY = 'abcdef1234'
from django.http import JsonResponse
from btoken.views import make_token
from user.models import UserProfile



# *methonds  可接受任意参数
# **kwargs 可接受多个key-words 传参
def loging_check(*methods):
    def loging_check(func):
        def wrapper(request,*args,**kwargs):
            #token 放在 request header -> authorization
            # 校验token,pyjwt 注意 异常检测
            # token 校验成功 , 进入视图函数
            # request.user = user
            token = request.META.get('HTTP_AUTHORIZATION')
            if not methods:
                #如果没传methods参数,则直接返回视图
                return func(request,*args,**kwargs)

            if not request.method in methods:
                    #如果当前请求的方法不在methods内则返回视图
                return func(request,*args,**kwargs)
            #严格判断大小写,统一大写
            #严格检查methods里的参数是 POST,GET,PUT,DELETE
            #token校验
            if not token :
                result = {'code':107,'error':'Please give me token'}
                return JsonResponse(result)
            #校验token,pyjwt 注意异常检测

            try:
                res = jwt.decode(token,KEY,algorithms='HS256')
            except Exception as e:
                print("token error is:--->%s"%e)
                result = {'code':108,'error':'Please login'}
                return JsonResponse(result)
            #校验失败


            #校验成功
            username = res['username']
            user = UserProfile.objects.get(username=username)
            request.user =user
            return func(request,*args,**kwargs)
        return wrapper
    return loging_check



def get_user_by_request(request):
    """

    :param request:
    :return:
    """
    token = request.META.get('HTTP_AUTHORIZATION')

    if not token or token == 'null':
        return None
    try:
        res = jwt.decode(token,KEY,algorithms='HS256')
    except Exception as e:
        print( '--get_user_by_request -jwt decode error is %s'%e)
        return None

    #获取token中的用户名
    username =res['username']
    user = UserProfile.objects.get(username=username)
    return user
