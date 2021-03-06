"""DjangoProject1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url, include
from django.contrib import admin
#1.9后,改了去掉了views ,login,logout放在了auth模块 错错错 ,还可以用,具有不同参数而已
# 登陆认证用的就是有views的,具体查看源码
# from django.contrib.auth import authenticate, login,logout

# from django.contrib.auth import views as auth_views
#自动寻找/
admin.autodiscover()

urlpatterns = [
    #url第二個參數不需要加'' 过期的做法 ,1.9直接引用
    url(r'^admin/', admin.site.urls),
    url(r'', include('blog.urls')),
    url(r'^accounts/login/$','django.contrib.auth.views.login' ),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'^search/', include('haystack.urls')),
]
