""" API endpoints for lensverse.stories """

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from lensverse.stories.models import Story
from lensverse.stories.serializers import StorySerializer


# Create your views here.
class StoryViewSet(ModelViewSet):
    """Create, read, update and delete stories"""

    queryset = Story.objects.all()
    serializer_class = StorySerializer
    permission_classes = [IsAuthenticated]
    ordering_fields = ["created_at"]
    filterset_fields = ["user"]
