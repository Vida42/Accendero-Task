from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    summary = models.CharField(max_length=200, blank=True)
    body = models.TextField()
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title