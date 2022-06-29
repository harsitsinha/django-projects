from django.db import models

# Create your models here.

class Comment(models.Model):
    username = models.CharField(max_length=100)
    comment = models.TextField()
    movie = models.CharField(max_length=100)
