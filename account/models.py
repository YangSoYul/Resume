from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Applicant(AbstractUser):
    age = models.IntegerField()  # 나이
    school = models.CharField(max_length=50)
    major = models.CharField(max_length=100)
    grade = models.CharField(max_length=50)
    like = models.CharField(max_length=100)
