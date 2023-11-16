""" API endpoints for pixhub """


from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from pixhub.models import User
from pixhub.serializers import UserSerializer


# Create your views here.
class UserViewSet(ModelViewSet):
    """User View Set"""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
