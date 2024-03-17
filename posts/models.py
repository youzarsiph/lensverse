""" Data Models for lensverse.posts """

from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
User = get_user_model()


class Post(models.Model):
    """Pix Posts"""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="posts",
        help_text="Post Owner",
    )
    image = models.ImageField(
        help_text="Post Image",
        upload_to="files/posts/images/",
    )
    text = models.CharField(
        max_length=128,
        null=True,
        blank=True,
        help_text="Post Text",
    )
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return super().__str__()
