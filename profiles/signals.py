from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from profiles.models import Profile


"""Using receiver decorators so craete_profile function will be triggered
every time a post save signal is sent wich will be sent evey time a user 
instance is created or updated"""


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """This fucntion is incharge of creating a new profile instance
    every time a user instance is created"""

    if created:
        Profile.objects.create(user=instance)
