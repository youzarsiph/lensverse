""" Serializers for lensverse.stories """

from rest_framework.serializers import ModelSerializer
from lensverse.stories.models import Story


# Create your serializers here.
class StorySerializer(ModelSerializer):
    """Story Serializer"""

    class Meta:
        """Meta data"""

        model = Story
        read_only_fields = ["user"]
        fields = ["id", "url", "user", "text", "image", "created_at", "updated_at"]
