"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, re_path
# django.conf.urls import urls 는  4.0이상 버전에서 삭제 됨
# 쉬운 수정 방법은 re_path를 사용하는 것
# 인프런 장고에선 urls를 사용하는데 
# re_path로 하는게 없음
from . import views

app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # URLconf
    # ex: /polls/5/
    path('<question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<question_id>/vote/', views.vote, name='vote'),
    # specifics
    # path('specifics/<question_id>/', views.detail, name='detail'),
]
