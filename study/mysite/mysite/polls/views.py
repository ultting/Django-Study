from re import template
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render

from .models import Question

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html') 템플릿 호출
    context = {'latest_question_list' : latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    
    return HttpResponse(f"You're looking at question {question_id}.")

def results(request, question_id):
    response = f"You're looking at the results of question {question_id}."
    return HttpResponse(response)

def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}.")
