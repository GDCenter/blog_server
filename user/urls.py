from django.urls import path
from  . import views
urlpatterns = [
    path('',views.users,name='users'),
    path('/<username>',views.users,name='user'),
    path('/<username>/avatar',views.user_avatar,name='user_avatar'),
]