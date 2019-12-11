import os
from django.http import HttpResponse
from django.shortcuts import render


def post_list(request):
    # HttpResponse는 클래스 이다.
    # djangogirls 의 templates 폴더 안에 있는 post_list.html파일의 내용을 read()한 결과를 HttpResponse에 인자로 전달

    # 경로 이동
    # os.path.abspath(__file__) <-- 현재 파일의 까지의 절대 경로
    # os.path.dirname(path) : 현재 파일을 포함하고 있는 경로, 즉 상위 경로
    # os.path.join : 경로 추가해 주기

    # 파일 열기
    # open
    cur_file_path = os.path.abspath(__file__)
    blog_dir_path = os.path.dirname(cur_file_path)
    root_dir_path = os.path.dirname(blog_dir_path) # 루트 디렉토리
    templates_dir_path = os.path.join(root_dir_path, 'templates')
    post_list_html_path = os.path.join(templates_dir_path, 'post_list.html')

    print(cur_file_path)
    print(blog_dir_path)


    f = open(post_list_html_path, 'rt')
    html = f.read()
    f.close()
    return HttpResponse(html)

