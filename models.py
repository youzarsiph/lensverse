""" Data Models for pixhub """


from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    """PixHub Users"""

    photo = models.ImageField(
        null=True,
        blank=True,
        help_text="User Photo",
        upload_to="files/images/users/",
    )
    bio = models.CharField(
        max_length=256,
        null=True,
        blank=True,
        help_text="Tell us about yourself",
    )
    followers = models.ManyToManyField(
        "self",
        through="followers.follower",
        related_name="followers",
    )
