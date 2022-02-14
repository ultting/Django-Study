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
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choiceText = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self): # __unicode__ on Python2
        return self.choiceText
    
    
class Article(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    contents = models.TextField()
    url = models.URLField()
    email = models.EmailField()
    cdate = models.DateTimeField(auto_now_add=True)