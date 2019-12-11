from django.http import HttpResponse
from django.shortcuts import render


def post_list(request):
    #HttpResponse는 클래스 이다.
    return HttpResponse('<html><body><h1>Post List</h1></body></html>')
