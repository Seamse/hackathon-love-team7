from django.db import models
from django.contrib.auth.models import User



class Profile(models.Model):

    """
    A user Profile model for maintaining default
    information and history
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio = models.TextField(default='', max_length=100)
    
    def __str__(self):
        return f'{self.user.username} Profile'

# @receiver(post_save, sender=User)
# def create_or_update_user_profile(sender, instance, created, **kwargs):
#     Profile.objects.create(user=instance)

#     """
#     Create or update user profiles
#     """
#     if created:
#         #Exisiting users: just save profile
#         instance.userprofile.save()
 