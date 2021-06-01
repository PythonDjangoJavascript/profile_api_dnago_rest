from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """Define Profile Database Model"""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=30, blank=True)
    avatar = models.ImageField(null=True, blank=True)

    def __str__(self) -> str:
        return self.user.username


class ProfileStatus(models.Model):
    """Define Profile status Database Model"""

    user_profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    status_content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'statuses'

    def __str__(self) -> str:
        return str(self.user_profile)
