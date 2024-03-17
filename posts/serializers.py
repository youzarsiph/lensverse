""" Serializers for lensverse.posts """

from rest_framework.serializers import ModelSerializer
from lensverse.posts.models import Post


# Create your serializers here.
class PostSerializer(ModelSerializer):
    """Pix Serializer"""

    class Meta:
        """Meta data"""

        model = Post
        read_only_fields = []
        fields = []
