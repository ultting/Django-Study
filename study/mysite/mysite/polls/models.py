import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    questionText = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self): # __unicode__ on Python2
        return self.questionText
    
    def was_published_recently(self):
        # https://stackoverflow.com/questions/27253339/problems-while-following-the-instructions-of-django-official-documentation
        # python manage.py shell 사용
        # was_published_recently() 의 값이 false로 나올경우 1일 미만일 경우
        return self.pub_date <= timezone.now() - datetime.timedelta(days=1)
    
    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choiceText = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    # python manage.py sqlmigrate 를 이용해 테이블을 확인한 후 변수명이랑 동일한지 확인
    def __str__(self): # __unicode__ on Python2
        return self.choiceText
    
    
# class Article(models.Model):
#     name = models.CharField(max_length=50)
#     title = models.CharField(max_length=50)
#     contents = models.TextField()
#     url = models.URLField()
#     email = models.EmailField()
#     cdate = models.DateTimeField(auto_now_add=True)

# 회원가입
class Register(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    password = models.CharField(max_length=10)
    nick = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=40)