""" Data Models for pixhub.pixes """


from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
User = get_user_model()


class Pix(models.Model):
    """Pix Posts"""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="pixes",
        help_text="Pix Owner",
    )
    image = models.ImageField(
        help_text="Pix Image",
        upload_to="files/pixes/images/",
    )
    text = models.CharField(
        max_length=128,
        null=True,
        blank=True,
        help_text="Pix Text",
    )
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return super().__str__()
