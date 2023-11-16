""" API endpoints for pixhub.profiles """


from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from pixhub.profiles.models import Profile
from pixhub.profiles.serializers import ProfileSerializer


# Create your views here.
class ProfileViewSet(ModelViewSet):
    """Create, read, update and delete profiles"""

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ["name", "description"]
    ordering_fields = ["created_at"]
    filterset_fields = ["name", "user"]
