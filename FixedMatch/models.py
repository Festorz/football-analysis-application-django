import random
import string
import os


from django.conf import settings
from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser, BaseUserManager
from django_countries.fields import CountryField
from django.core import serializers
import json

record_category = (
    ('MT', 'Matches'),
    ('RS', 'Match Results'),

)

prediction_level = (
    ('PR', 'Premium'),
)
description_category = (
    ('MT', 'Matches'),
    ('PR', 'Predictions'),
)

def create_slug_code():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, username, first_name, last_name, email, phone, country, password):
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, phone=phone, country=country, first_name=first_name,
                          last_name=last_name)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, username, email, phone, password, country=None, first_name=None, last_name=None):
        user = self.create_user(username=username, email=email, phone=phone, password=password, country=country,
                                first_name=first_name, last_name=last_name)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class User(PermissionsMixin, AbstractBaseUser):
    username = models.CharField(max_length=32, unique=True, )
    email = models.EmailField(max_length=32)
    phone = models.CharField(max_length=13, blank=False)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    country = CountryField(multiple=False, null=True, blank=True)
    is_premium = models.BooleanField(default=False)
    payment_code = models.CharField(max_length=100, null=True, blank=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    REQUIRED_FIELDS = ["email", "phone"]
    USERNAME_FIELD = "username"
    objects = UserManager()

    def __str__(self):
        return self.username


class Match(models.Model):
    title = models.CharField(max_length=50, default='')
    match_file = models.FileField()
    category = models.CharField(choices=record_category, max_length=3, default='')

    def __str__(self):
        return self.title

    def entry_saved_data(self):
        return json.load(self.match_file)

    class Meta:
        verbose_name_plural = 'Matches'


class Prediction(models.Model):
    title = models.CharField(max_length=50, default='')
    prediction_file = models.FileField(default='')
    prediction_category = models.CharField(choices=prediction_level, max_length=3)

    def __str__(self):
        return self.title

    def entry_saved_data(self):
        return json.load(self.prediction_file)


class MatchDescription(models.Model):
    title = models.CharField(max_length=50, default='')
    description_file = models.FileField()
    category = models.CharField(choices=description_category, max_length=2, default='')

    def __str__(self):
        return self.title



class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    slug = models.SlugField(default=create_slug_code, blank=False, editable=False)
    intro = models.TextField(default='')
    body = models.TextField(default='')
    date_added = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_added']

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    comment = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['date_added']




    
