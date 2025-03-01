""" Data Models for lensverse.tags """

from django.db import models


# Create your models here.
class Tag(models.Model):
    """Post Tags"""

    name = models.CharField(
        max_length=32,
        unique=True,
        db_index=True,
        help_text="Topic Name",
    )
    description = models.CharField(
        max_length=256,
        null=True,
        blank=True,
        help_text="Topic Description",
    )
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
