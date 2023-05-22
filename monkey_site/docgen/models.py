from django.db import models

# Create your models here.
class Document(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    patronymic = models.CharField(max_length=100, blank=True)
    sex = models.CharField(max_length=6)
    birthday = models.CharField(max_length=10)
    inputState = models.CharField(max_length=2)
    metadata = models.BooleanField()
    
class Image(models.Model):
    filename = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)