from django.http import HttpResponse
from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Welcome! This page url Create or Read')

def create(request):
    return HttpResponse('Create')

def read(request, id):
    return HttpResponse('Read'+str(id))