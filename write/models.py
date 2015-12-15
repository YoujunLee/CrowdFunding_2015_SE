from django.db import models
from login.models import *
# Create your models here.
class WriteData(models.Model):
    user=models.ForeignKey(Profile)
    Name = models.CharField(max_length=30)
    distribute = models.CharField(max_length=30)
    duedate = models.CharField(max_length=100)
    bank = models.CharField(max_length=30)
    putmoney= models.IntegerField(default=0)
    money = models.IntegerField()
    text = models.TextField()
   