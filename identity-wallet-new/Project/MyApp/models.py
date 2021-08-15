from django.db import models
from django import forms
from datetime import date

# Create your models here.
class User(models.Model):
    email = models.EmailField(max_length=120, default="")