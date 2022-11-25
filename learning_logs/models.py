from django.db import models

# Create your models here.
class Topic(models.Model):
    "The topic learnt."
    topic = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    
class Subject(models.Model):
    "The subject in the topic that was learnt."
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    
class Entry(models.Model):
    "Entry of what was learnt."
    subject = models.ForeignKey(Subject, on_delete = models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    