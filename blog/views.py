from django.http import HttpResponse
from django.shortcuts import render


def post_list(request):
    #HttpResponse는 클래스 이다.
    return HttpResponse('<html>'
                        '<body>'
                        '<h1>Post List</h1>'
                        '<div><p>published:12.11.2019</p>'
                        '<h2><a href=#>My first post</a></h2>'
                        '<div><p>published:12.12.2019</p>'
                        '<h2><a href=#>My second post</a></h2>'
                        '</body>'
                        '</html>')
