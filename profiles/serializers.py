""" Serializers for lensverse.profiles """

from rest_framework.serializers import ModelSerializer
from lensverse.profiles.models import Profile


# Create your serializers here.
class ProfileSerializer(ModelSerializer):
    """Profile Serializer"""

    class Meta:
        """Meta data"""

        model = Profile
        read_only_fields = ["user"]
        fields = [
            "id",
            "url",
            "user",
            "name",
            "description",
            "created_at",
            "updated_at",
        ]
