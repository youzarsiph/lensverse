""" Data Models for lensverse.stories """

from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
User = get_user_model()


class Story(models.Model):
    """Stories"""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="stories",
        help_text="Story Owner",
    )
    text = models.CharField(
        max_length=256,
        null=True,
        blank=True,
        help_text="Story Text",
    )
    image = models.ImageField(
        null=True,
        blank=True,
        help_text="Story Image",
        upload_to="files/stories/images/",
    )
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return super().__str__()
