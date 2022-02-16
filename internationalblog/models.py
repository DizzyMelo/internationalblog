import datetime

from django.db import models
from django.utils import timezone
# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=30)
    status = models.BooleanField()

    def __str__(self) -> str:
        return self.name

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    post_title = models.CharField(max_length=200)
    post_message = models.CharField(max_length=1000)
    post_date = models.DateTimeField('date posted')
    status = models.BooleanField()

    def __str__(self) -> str:
        return self.post_title

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)