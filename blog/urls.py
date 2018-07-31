from django.urls import  path
from . import views
from django.conf.urls import  url


urlpatterns = [
    # post_list라는 이름의 view가 ^$ URL에 할당됨.
    # 누군가 http://127.0.0.1:8000/ 주소로 들어오면 views.post_list를 보여주라고 말하는것
    path('', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
]