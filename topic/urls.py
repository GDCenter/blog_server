from django.urls import path
from django.conf.urls import re_path
from  . import views
urlpatterns =[
    #/v1/topic/author_id - index 首页
    path('/<author_id>',views.topics,name='topic'),
    path('',views.topics,name='topic'),
    path('/<author_id>/<t_id>',views.topics),
    re_path(r'/(?P<author_id>[\w]+)$',views.topics),

]