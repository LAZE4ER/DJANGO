from django.db import models

# Create your models here.


class Bug(models.Model):
    STATUS_CHOICES = [
        ('New', 'New'),
        ('In Progress', 'In Progress'),
        ('Resolved', 'Resolved'),
        ('Closed', 'Closed'),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField()
    severity = models.IntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='New')    
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    