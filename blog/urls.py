from django.urls import  path
from . import views

urlpatterns = [
    # post_list라는 이름의 view가 ^$ URL에 할당됨.
    # 누군가 http://127.0.0.1:8000/ 주소로 들어오면 views.post_list를 보여주라고 말하는것
    path('', views.post_list, name='post_list')
]