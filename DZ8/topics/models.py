from django.db import models
from django.contrib.auth.models import User
from django.db.models import ManyToManyField
# Create your models here.


    


class Topic(models.Model):
    name = models.CharField(max_length=100, unique=True)
    subscribers = ManyToManyField(User, related_name='subscribed_topics')
    def __str__(self):
        return self.name


class TopicActivity(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='activities')
    action =  models.CharField(max_length=20, choices=[('created', 'Created'), ('updated', 'Updated'), ('deleted', 'Deleted')])
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.action} in {self.topic.name}"