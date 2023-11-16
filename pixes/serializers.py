""" Serializers for pixhub.pixes """


from rest_framework.serializers import ModelSerializer
from pixhub.pixes.models import Pix


# Create your serializers here.
class PixSerializer(ModelSerializer):
    """Pix Serializer"""

    class Meta:
        """Meta data"""

        model = Pix
        read_only_fields = []
        fields = []
