from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class Profile(models.Model):
    parent_user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=100, default="Male")
    dept = models.CharField(max_length=100, default="None")
    hostel = models.CharField(max_length=100, default="None")
    image = models.ImageField(default='default.jpg',upload_to='profile-pics')
    bio = models.TextField(default='', max_length=200)

    def __str__(self):
        return self.parent_user.username

    def full_name(self):
        return self.first_name + ' ' + self.last_name
