""" Data Models for lensverse.profiles """

from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
User = get_user_model()


class Profile(models.Model):
    """Profiles"""

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        help_text="Profile Owner",
    )
    name = models.CharField(
        max_length=32,
        unique=True,
        db_index=True,
        help_text="Profile Name",
    )
    description = models.CharField(
        max_length=256,
        null=True,
        blank=True,
        help_text="Profile Description",
    )
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
