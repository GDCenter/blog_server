import datetime

from django.http import JsonResponse
from django.shortcuts import render
from tools.loging_decorator import loging_check
import json
from user.models import UserProfile

from topic.models import Topic
from .models import Msg_board
# Create your views here.

@loging_check('POST','GET')
def message_board(request,topic_id):
    if request.method =='POST':
        user = request.user
        # 拿数据
        # user = UserProfile.objects.get(username=user)

        json_str = request.body
        if not json_str:
            # 判断字符串是否为空
            result = {'code': 401, 'error': 'Please give me request message'}
            return JsonResponse(result)
        json_obj = json.loads(json_str)

        #获取留言内容
        content = json_obj.get('content')
        parent_id = json_obj.get('parent_id')
        if not content:
            result = {'code':403,'error':'Please give me content'}
            return JsonResponse(result)
        #当前时间
        now = datetime.datetime.now()

        try:
            topic = Topic.objects.get(id=topic_id)
        except Exception as e:
            result = {'code':404,'error':'This topci is not existed'}
            return JsonResponse(result)
        #判断当前topic limit
        if topic.limit=='private':
            #如果当前limit是私有的,则必须为博主方可评论
            if user.username != topic.author.username:
                result = {'code':405,'error':'Please go out !'}
                return JsonResponse(result)
        Msg_board.objects.create(topic=topic,
                                 content=content,
                                 parent_message=parent_id,
                                 created_time=now,
                                 publisher=user)
        return JsonResponse({'code':200,'error':{}})



    #请求获取博客内容
    elif request.method =='GET':
        author = request.user
