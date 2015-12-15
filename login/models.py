# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings

class Profile(models.Model):
    class Meta:
        verbose_name = u'프로필'
        verbose_name_plural = u'프로필'
    
    User = models.OneToOneField(settings.AUTH_USER_MODEL)
    Name = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    hint = models.CharField(max_length=100)
    answer = models.CharField(max_length=30)
    
    
    def __unicode__(self):
        return self.User.username


# Create your models here.
