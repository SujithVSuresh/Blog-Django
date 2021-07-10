from django.db import models
from django.utils import timezone #for changing thr dateTime if we want
from django.contrib.auth.models import User #importing user model

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE) #if author is deleted, then post is also deleted.

    def __str__(self):
        return self.title

