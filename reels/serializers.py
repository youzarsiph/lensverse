""" Serializers for lensverse.reels """

from rest_framework.serializers import ModelSerializer
from lensverse.reels.models import Reel


# Create your serializers here.
class ReelSerializer(ModelSerializer):
    """Reel Serializer"""

    class Meta:
        """Meta data"""

        model = Reel
        read_only_fields = ["user"]
        fields = ["id", "url", "user", "video", "created_at", "updated_at"]
