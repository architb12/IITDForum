from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import datetime

# Create your models here.
# Model for Post
class Post(models.Model):
    title = models.CharField(max_length = 50)
    text = models.CharField(max_length = 500)
    likers = []
    likes_count = models.IntegerField(default = 0)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    pub_date = models.DateTimeField(default = timezone.now())

    def __str__(self):
        return self.title

class Comment(models.Model):
    parent_post = models.ForeignKey(Post, on_delete = models.CASCADE)
    text = models.CharField(max_length = 500)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    likers = []
    likes_count = models.IntegerField(default = 0)
    pub_date = models.DateTimeField(default = timezone.now())
