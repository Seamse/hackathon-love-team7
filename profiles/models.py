from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



class Profile(models.Model):

    """
    A user Profile model for maintaining default
    information and history
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio = models.TextField(default='', max_length=100, null=True, blank=True)
   
    
    def __str__(self):
        return f'{self.user.username} Profile'

