from django.http import JsonResponse
from btoken.views import make_token
from user.models import UserProfile
import json
import jwt




def users(request,username=None):
    if request.method == 'GET':
        #取数据
        #/v1/user/guoxiaonao?info=1&email=1
        #       {'info':xxx,'email':xxx}
        if username:
            #具体用户数据
            # /


            try:
                user = UserProfile.objects.get(username=username)
            except UserProfile.DoesNotExist:
                user = None

            if not user:
                result = {'code':208,'error':'The user is not existed'}
                return JsonResponse(result)


            #判断查询字符串
            if request.GET.keys():
                #证明由查询字符串
                data = {}
                for k in request.GET.keys():
                    if hasattr(user,k):
                        data[k] = getattr(user,k)
                result = {'code':200,'username':username,'data':data}
                return  JsonResponse(result)
            else:
                #证明指定查询用户全量数据
                result = {'code':200,'username':username,'data:':{
                    'info':user.info,'sign':user.sign,'nickname':user.nickname,
                    'avatar': str(user.avatar)
                }}
                return JsonResponse(result)

        else:
            #全部用户数据
            #UserProfiel 获取全部用户数据
            all_users = UserProfile.objects.all()
            res = []
            for u in all_users:
                d = {}
                d['username']=u.username
                d['email']=u.email
                res.append(d)
            #[{username:xxxx},{username"xxxx},{username:xxx}]
            result = {'code':200,'data':res}
            return JsonResponse(result)




def test_api(request):
    #JsonResponse 1,将返回内容序列化成json
    #2.response中添加conten-type
    return JsonResponse({'code':200})