""" API endpoints for pixhub.topics """


from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from pixhub.topics.models import Topic
from pixhub.topics.serializers import TopicSerializer


# Create your views here.
class TopicViewSet(ModelViewSet):
    """Create, read, update and delete Topics"""

    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ["name", "description"]
    ordering_fields = ["created_at", "updated_at"]
    filterset_fields = ["name"]

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            self.permission_classes += [IsAdminUser]

        return super().get_permissions()
