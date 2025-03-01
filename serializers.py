""" Serializers for lensverse """

from rest_framework.serializers import ModelSerializer
from lensverse.models import User


# Create your serializers here.
class UserSerializer(ModelSerializer):
    """User Serializer"""

    class Meta:
        """Meta data"""

        model = User
        fields = [
            "id",
            "url",
            "username",
            "first_name",
            "last_name",
            "date_joined",
            "last_login",
        ]
