""" Serializers for pixhub.topics """


from rest_framework.serializers import ModelSerializer
from pixhub.topics.models import Topic


# Create your serializers here.
class TopicSerializer(ModelSerializer):
    """Topic Serializer"""

    class Meta:
        """Meta data"""

        model = Topic
        fields = ["id", "url", "name", "description", "created_at", "updated_at"]
