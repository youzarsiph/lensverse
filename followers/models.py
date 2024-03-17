""" Data Models for lensverse.followers """

from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
User = get_user_model()


class Follower(models.Model):
    """Followers"""

    from_user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="following",
        help_text="Follower",
    )
    to_user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="followers",
        help_text="Followed",
    )
    is_approved = models.BooleanField(
        default=False,
        help_text="Designates if the follow request is approved",
    )
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return super().__str__()
