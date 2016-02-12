#博客的控制器  中转站, 附带上下文内容

from django.conf.urls import patterns, include, url
from . import views

#后面的name属性有什么作用呢?
#作用在于html中的url时,执行定对应的名字即可,转到这里来进行控制处理
#例如:href="{% url 'post_edit' pk=post.pk %} 就会转到控制器这里来处理
#?用于传参数www.baidu.com/login?n=1等等

#为什么要/后面加一个/edit
urlpatterns = [
    # url(r'^$', views.listing),#test for paginator
    url(r'^$', views.post_list),
    #P<pk>为是post/pk  其中pk的值会具体的值给替代掉 ,这个值就是具体 post对象的.pk值
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^drafts/$', views.post_draft_list, name='post_draft_list'),
    url(r'^post/(?P<pk>[0-9]+)/publish/$', views.post_poblish, name='post_publish'),
    url(r'^post/(?P<pk>[0-9]+)/remove/$', views.post_remove, name='post_remove'),
    url(r'^post/search/$',views.full_search)
]