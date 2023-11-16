""" Data Models for pixhub.reels """


from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import FileExtensionValidator


# Create your models here.
User = get_user_model()


class Reel(models.Model):
    """Reels"""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="reels",
        help_text="Reel Owner",
    )
    video = models.FileField(
        help_text="Reel Image",
        upload_to="files/reels/videos/",
        validators=[FileExtensionValidator(["mp4"], "This file is not a video.")],
    )
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return super().__str__()
