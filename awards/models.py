from django.db import models

from django.db import models

import datetime as dt
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.core.validators import MaxValueValidator,MinValueValidator

from django.db.models.signals import post_save

from django.db.models import Q

class Profile(models.Model):
    user = models.OneToOneField(User,null=True,related_name='profile')
    prof_pic = models.ImageField(upload_to = 'ards/',default='Profile Pic')
    bio = models.CharField(max_length=300)
    contact = models.CharField(max_length=30)
    pub_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.user

    def save_profile(self):
        self.save()

    def create_profile(sender,instance,created,**kwargs):
        if created:
            Profile.objects.create(user=instance)

    post_save.connect(create_profile,sender=User)
        # user = request.user
        # profile = Profile.objects.filter(user=user).first()
        # return profile
# Create your models here.
