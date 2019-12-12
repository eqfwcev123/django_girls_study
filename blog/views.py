import os

from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse

from blog.models import Post
from django.http import HttpResponseRedirect

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

    # posts 라는 변수에 전체 post 를 가지는 QuerySet객체를 할당.
    # hint) Post.objects.무언가 ...를 실행한 결과는 querySet 객체가 된다.
    # conext 라는 딕셔너리를 생성하며, 'posts'키에 위 post 변수를 value도록 한다
    # 3. render 의 3번째 위치인자로 위 context 변수를 할당한다.
    from blog.models import Post
    posts = Post.objects.all().order_by('-pk')
    context = {
        'posts': posts,
    }
    #context 에 있는 값들이 template_engine 에 넘어간다. post_list.html 에 보면 posts 라고 있는데, 그게 context 딕셔너리에 있는 posts에서 온다.

    return render(request, 'post_list.html', context)

# def render(request, template_name, context=None, content_type=None, status=None, using=None):
#     """
#     Return a HttpResponse whose content is filled with the result of calling
#     django.template.loader.render_to_string() with the passed arguments.
#     """
#     content = loader.render_to_string(template_name, context, request, using=using)
#     return HttpResponse(content, content_type, status)
#
#     context = A dictionary of values to add to the template context. By default, this is an empty dictionary.
#     If a value in the dictionary is callable, the view will call it just before rendering the templat

def post_detail(request, pk):
    print('post_detail request : ', request)
    print('post_detail pk: ', pk)
    try:
        post = Post.objects.get(id__exact= pk)
    except:
        return HttpResponse('<h1>해당 pk 를 가지고 있는 데이터가 없슴</h1>')

    context = {
        'posts': post,
    }

    return render(request, 'post_detail.html', context)


def post_add(request):
    if request.method == 'POST':
        author = request.user
        title = request.POST['title']
        text = request.POST['text']
        post = Post.objects.create(author=author, title=title, text=text) #쿼리셋 반환
        result = f'title: {post.title}, created_date:{post.created_date}'
        post_list_url = reverse('url-name-post-list')
        return HttpResponseRedirect(post_list_url) # /posts/ 로 우회
    else:
        return render(request, 'post_add.html')