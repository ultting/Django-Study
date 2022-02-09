# git 설치 후 내 git id와 name 을 입력
# 명령어는 git config -- global user.email "my email @ xxxx.com"
# git config -- global user.name "my nick"

# git에 push 하는 법
# Source Control -> + 클릭 -> Commit 메세지 -> Check 표시 

# Django 설치 하는 법
# 1. python 설치
# 2. pip install django
# 3. django-admin startproject ( project name )
# 가상환경이 가장 중요
# https://axce.tistory.com/65 장고 생성


# 현재 경로 기준 서버로 가는 명령어
# cd FirstProject -> cd firstproject

# 장고 서버 실행할떈 python manage.py runserver
# 서버를 멈추고 싶을땐 Ctrl+c
# 서버의 포트를 바꾸고 싶을땐 python manage.py runserver ####

# Django app 만들기
# project url.py -> app urls.py -> view def 
# 명령어 : django-admin startapp myapp

# Routing : 경로
# 흐름
# 현재 프로젝트 기준
# 장고가 페이지를 요청할 경우
# firstproject 에 있는 urls.py로 들어감
# 이때 include 함수로 인해 myapp urls.py로 위임
# 이후 myapp에 있는 경로를 호출 
# 그 다음 view로 이동한 후 맞는 함수를 실행
# 이때 httResponse 를 클라이언트에 호출

# - Database
# - Model(Django 내장)
# - Security 웹 보안
# - .py .html 코드 분리하기 위해 Template Engine 사용

# Django html 과 py 분리하기
# 해당 프로젝트안에 템플릿 폴더 생성 
# 생성폴더 안데 .html 파일 생성
# settings.py 에 templates 에 dirs 부분경로 수정
# views 에 render 를 이용해 연결

# 표준 라이브러리 import
from __future__ import absolute_import
from math import sqrt
from os.path import abspath
# 코어 장고 임포트
import Django
print(Django.__path__)
