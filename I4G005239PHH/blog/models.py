from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.urls import reverse
User = get_user_model()

# Create your models here.

...
class Post(models.Model):
    Title = models.CharField(max_length=200)
    Text = models.TextField()
    Author = models. ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField()
    Published_date = models.DateTimeField()
    
