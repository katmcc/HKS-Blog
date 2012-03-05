from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from PIL import Image
import os

class AuthorProfile(models.Model):
    # This is the only required field
    user = models.ForeignKey(User, unique=True)
    
    avatar = models.ImageField(upload_to='avatars')
    description = models.TextField()
    site = models.URLField(null=True, blank=True)
    
    #Social links
    facebook = models.CharField(max_length=200, null=True, blank=True)
    googleplus = models.CharField(max_length=200, null=True, blank=True)
    twitter = models.CharField(max_length=200, null=True, blank=True)
    tumblr = models.URLField(null=True, blank=True)
    pinterest = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
      app_label = 'accounts'

    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            AuthorProfile.objects.create(user=instance)
    
    post_save.connect(create_user_profile, sender=User)

def get_default_thumbnail_filename(filename):
	path, ext = os.path.splitext(filename)
	return path + '.thumb.jpg'
