from django.db import models

# Create your models here.

Gender_List = (
    ('남자','남자'),
    ('여자','여자'),
)

class applicant(models.Model):
   name = models.CharField(max_length=4) #이름
   age = models.IntegerField() #나이
   introduce = models.TextField()
   gender = models.CharField(max_length=2, choices=Gender_List)
   date = models.DateTimeField('resume submitted', null=True)
   