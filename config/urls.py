"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blog.views import post_list, post_detail, post_add

urlpatterns = [
    path('admin/', admin.site.urls),
    path('post-list/', post_list, name='post_list'),
    path('posts/', post_list, name='url-name-post-list'),
    # post-details 뒤에 오는것은 숫자인데, 이것을 pk로 하자!
    path('post-detail/<int:pk>/',post_detail, name='url-name-post-detail'),
    path('posts/add/',post_add, name='url-name-post-add')
]
