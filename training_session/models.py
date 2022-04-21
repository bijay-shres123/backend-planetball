from django.db import models

#Requested Training  Session
class RequestedSession(models.Model):
    title  =  models.CharField(max_length=30)
    description = models.CharField(max_length=100)
   
    