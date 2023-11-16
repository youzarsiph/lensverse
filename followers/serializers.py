""" Serializers for pixhub.followers """


from rest_framework.serializers import ModelSerializer
from pixhub.followers.models import Follower


# Create your serializers here.
class FollowerSerializer(ModelSerializer):
    """Follower Serializer"""

    class Meta:
        """Meta data"""

        model = Follower
        read_only_fields = ["from_user", "to_user", "is_approved"]
        fields = [
            "id",
            "url",
            "from_user",
            "to_user",
            "is_approved",
            "created_at",
            "updated_at",
        ]
