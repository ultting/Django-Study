
from django.http import HttpResponse
from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt # 면제
 
import random

# Create your views here.
nextId = 4
topics = [
    # 딕셔너리 형태의 데이터
    {'id':1, 'title':'routing','body':'Routing is ...'},
    {'id':2, 'title':'view','body':'View is ...'},
    {'id':3, 'title':'Model','body':'Model is ...'},
]

def HTMLTemplate(articleTag, id=None):
    global topics # 전역변수 지정
    ol = ''
    contextUI = ''
    if id != None:
        contextUI = f'''
            <li>
                <form action="/delete/" method="post">
                    <input type="hidden" name="id" value={id}>
                    <input type="submit" value="delete">
                </form>
            </li>
            <li>
                <a href="/update/{id}">update</a>
            </li>
        '''
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
        <ul>
            <li><a href="/create/">create</a></li>
            {contextUI}
        </ul>
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

def read(request, id):
    global topics
    article = ''
    for topic in topics:
        if topic['id'] == int(id): # request로 들어오는 id는 String
            article = f'<h2>{topic["title"]}</h2>{topic["body"]}'
    
    return HttpResponse(HTMLTemplate(article, id))

@csrf_exempt
def create(request):
    global nextId
    if request.method=='GET':
        article='''
            <form action="/create/" method="post">
                <p><input type="text" name="title" placeholder="title"></p>
                <p><textarea name="body" placeholder="body"></textarea></p>
                <p><input type="submit"></p>
            </form>
            
        '''
        return HttpResponse(HTMLTemplate(article))
    elif request.method =='POST' : 
        title = request.POST['title']
        body = request.POST['body']
        newTopic = {"id":nextId,"title":title,"body":body}
        topics.append(newTopic)
        url = '/read/'+str(nextId)
        nextId+=1
        return redirect(url)

@csrf_exempt
def delete(request):
    global topics
    if request.method == 'POST':
        id = request.POST['id']
        newTopics = []
        for topic in topics:
            if topic['id'] != int(id):
                newTopics.append(topic)
        topics = newTopics
        return redirect('/')
    
@csrf_exempt
def update(request, id):
    global topics
    if request.method=='GET':
        for topic in topics:
            if topic['id'] == int(id):
                selectedTopic = {
                    "title":topic['title'],
                    "body":topic['body']
                }
        article=f'''
            <form action="/update/{id}/" method="post">
                <p><input type="text" name="title" value={selectedTopic["title"]}></p>
                <p><textarea name="body" placeholder="body">{selectedTopic["body"]}</textarea></p>
                <p><input type="submit"></p>
            </form>
            
        '''
        return HttpResponse(HTMLTemplate(article, id))
    elif request.method =='POST':
        title = request.POST['title']
        body = request.POST['body']
        for topic in topics:
            if topic['id'] == int(id):
                topic['title'] = title
                topic['body'] = body
        return redirect(f'/read/{id}')
    