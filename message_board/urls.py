from django.conf.urls import re_path
from django.urls import path
from . import views
urlpatterns =[
    path('/<topic_id>',views.message_board,name='messages'),
]