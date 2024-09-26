from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse  
from datetime import datetime,time
# Create your models here.


class Post(models.Model):
    title=models.CharField(max_length=255)
    title_page=models.CharField(max_length=255, default="title_page")
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    body=models.TextField()
    date_post=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title +" | " + str(self.author)
    
    def get_absolute_url(self):
        return reverse('article_detail',args=str((self.id)))
        