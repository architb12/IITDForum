from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import datetime

# Create your models here.
# Model for Post
class Post(models.Model):
    text = models.TextField(max_length = 5000)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    pub_date = models.DateTimeField(default = timezone.now())
    def __str__(self):
        return str(self.pub_date) + ' by ' + self.author.username

class Comment(models.Model):
    parent_post = models.ForeignKey(Post, on_delete = models.CASCADE)
    text = models.CharField(max_length = 500)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    pub_date = models.DateTimeField(default = timezone.now())

class PostLike(models.Model):
    parent_post = models.OneToOneField(Post, on_delete=models.CASCADE)
    likers = models.ManyToManyField(User, blank=True)
    
    def __str__(self):
        return str(self.parent_post) + ' (' + str(self.likers.count()) + ')'
