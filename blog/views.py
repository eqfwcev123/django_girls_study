import os
from django.http import HttpResponse
from django.shortcuts import render

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print('setting.py dml BASE_DIR 는: ', BASE_DIR)
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
print('setting.py dml TEMPLATES_DIR 는: ', TEMPLATES_DIR)


def post_list(request):
    # HttpResponse는 클래스 이다.
    # djangogirls 의 templates 폴더 안에 있는 post_list.html파일의 내용을 read()한 결과를 HttpResponse에 인자로 전달

    # 경로 이동
    # os.path.abspath(__file__) <-- 현재 파일의 까지의 절대 경로
    # os.path.dirname(path) : 현재 파일을 포함하고 있는 경로, 즉 상위 경로
    # os.path.join : 경로 추가해 주기

    # Template을 찾을 경로에서
    # post_list.html을 찾아서
    # 그 파일을 텍스트로 만들어서 HttpResponse형태로 돌려준다
    # 위 기능을 하는 shortcut 함수

    #posts 라는 변수에 전체 post 를 가지는 QuerySet객체를 할당.
    # hint) Post.objects.무언가 ...를 실행한 결과는 querySet 객체가 된다.
    # conext 라는 딕셔너리를 생성하며, 'posts'키에 위 post 변수를 value도록 한다
    # 3. render 의 3번째 위치인자로 위 context 변수를 할당한다.

    from blog.models import Post
    posts = Post.objects.all()
    context= {
        'posts':posts,
    }


    return render(request, 'post_list.html', context)

