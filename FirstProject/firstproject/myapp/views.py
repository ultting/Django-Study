
from django.http import HttpResponse
from django.shortcuts import render, HttpResponse
import random

# Create your views here.
topics = [
    # 딕셔너리 형태의 데이터
    {'id':1, 'title':'routing','body':'Routing is ...'},
    {'id':2, 'title':'view','body':'View is ...'},
    {'id':3, 'title':'Model','body':'Model is ...'},
]

def HTMLTemplate(articleTag):
    global topics # 전역변수 지정
    ol = ''
    for topic in topics:
        ol += f'<li><a href="/read/{topic["id"]}">{topic["title"]}</a></li>'
    
    return f'''
    <html>
    <body>
        <h1><a href="/">Django</a></h1>
        <ul>
           {ol}
        </ul>
        {articleTag}
    </body>
    </html>
    '''
def index(request):
        # '<h1>Random</h1>'+str(random.random()) << 페이지에 랜덤한 수 
    article = '''
    <h2>Welcome</h2>
    Hello, Django
    '''
    return HttpResponse(HTMLTemplate(article))

def create(request):
    return HttpResponse('Create')

def read(request, id):
    global topics
    article = ''
    for topic in topics:
        if topic['id'] == int(id): # request로 들어오는 id는 String
            article = f'<h2>{topic["title"]}</h2>{topic["body"]}'
    
    return HttpResponse(HTMLTemplate(article))