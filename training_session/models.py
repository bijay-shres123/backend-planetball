from django.db import models


#Requested Training  Session
class RequestedSession(models.Model):
    title  =  models.CharField(max_length=30)
    description = models.CharField(max_length=100)
   
class TrainingSession(models.Model):
    title = models.CharField(max_length=30)
    highlighted_info = models.CharField(max_length=200)
    youtube_link = models.URLField(max_length=100)
    description = models.CharField(max_length=1500)

#Ask Forum  Question
class AskQuestion(models.Model):
    title  =  models.CharField(max_length=30)
    description = models.CharField(max_length=300)