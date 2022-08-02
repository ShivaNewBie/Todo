from django.db import models

from django.contrib.auth.models import User

from django.conf import settings 
# Create your models here.


class Task(models.Model):
    description = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='task')
