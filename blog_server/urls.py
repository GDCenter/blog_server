"""blog_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from  . import views

from django.urls import include

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('test_api',views.test_api),
    path('v1/users',include('user.urls')),
    #添加btoken模块 URL映射.该模块登录操作
    # path('users',views.users),
    path('v1/token',include('btoken.urls')),
    path('v1/topics',include('topic.urls')),
    path('v1/messages',include('message_board.urls'))

]

# from django.conf import settings
# from django.conf.urls.static import static
urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
