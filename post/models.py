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

class Tag(models.Model):
    parent_user = models.ForeignKey(User, on_delete = models.CASCADE)
    tagger_id = models.CharField(max_length = 10, default = '1')
    tag_type = models.CharField(max_length = 10, default = 'post')
    pub_date = models.DateTimeField(default = timezone.now())
    post_id = models.CharField(max_length = 10, default = '1')
    seen = models.BooleanField(default = False)

    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return 'User with id ' + self.tagger_id + ' tagged ' + self.parent_user.username + ' on a ' + self.tag_type + ' at time ' + str(self.pub_date)

    def tagger_name(self):
        return User.objects.get(id=self.tagger_id).username

    def tagger_image(self):
        return User.objects.get(id=self.tagger_id).profile.image
    
    def post_author_name(self):
        return Post.objects.get(id=self.post_id).author.username