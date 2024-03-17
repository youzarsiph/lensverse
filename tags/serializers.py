""" Serializers for lensverse.tags """

from rest_framework.serializers import ModelSerializer
from lensverse.tags.models import Tag


# Create your serializers here.
class TagSerializer(ModelSerializer):
    """Tag Serializer"""

    class Meta:
        """Meta data"""

        model = Tag
        fields = ["id", "url", "name", "description", "created_at", "updated_at"]
