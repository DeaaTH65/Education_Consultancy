from django.db import models


# Create your models here.
class Message(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=255)
    
    def __str__(self):
        return self.subject
    