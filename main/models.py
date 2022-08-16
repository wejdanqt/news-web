from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
import uuid

# Create your models here.
from django.contrib.auth.base_user import BaseUserManager
from accounts.models import User


class Article(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255, blank=True, null=True)
    author = models.CharField(max_length=255, blank=True, null=True)
    content = models.CharField(max_length=500, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    published_at= models.DateTimeField(blank=True, null=True)
    url_to_image = models.ImageField(upload_to='gallery', max_length=800)
    favorites = models.ManyToManyField(
        User, related_name='favorites', default=None, blank=True)

    def __str__(self):
        return self.title
