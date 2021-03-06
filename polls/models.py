from __future__ import unicode_literals
from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    mod_date = models.DateTimeField('date modified')
    
    def __str__(self): # __str__ on python3
        return self.question_text
        
class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self): # __str__ on python3
        return self.choice_text
        
        