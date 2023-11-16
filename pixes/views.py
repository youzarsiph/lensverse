""" API endpoints for pixhub.pixes """


from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from pixhub.pixes.models import Pix
from pixhub.pixes.serializers import PixSerializer


# Create your views here.
class PixViewSet(ModelViewSet):
    """Create, read, update and delete Pixs"""

    queryset = Pix.objects.all()
    serializer_class = PixSerializer
    permission_classes = [IsAuthenticated]
    search_fields = []
    ordering_fields = []
    filterset_fields = []
