from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    # username = models.CharField(max_length=30)
    # password = models.CharField(max_length=16)
    nickname = models.CharField(max_length=30)
    friends = models.TextField(blank=True)
    email = models.EmailField(unique=True)
    is_confirmed = models.BooleanField(default=False)

    REQURIED_FIELDS = []

# description = models.TextField(blank=True)
# created_at = models.DateTimeField(auto_now_add=True)
# url = models.URLField()