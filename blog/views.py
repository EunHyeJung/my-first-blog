from django.shortcuts import render

# Create your views here.

# 요청(request)를 넘겨받아 render 메서드를 호출함.
# 이 함수를 호출하여 받은(return) blog/post_list.html 템플릿을 보여줌.
def post_list(request):
    return render(request, 'blog/post_list.html', {})