""" API endpoints for lensverse """

from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from lensverse.models import User
from lensverse.serializers import UserSerializer


# Create your views here.
class UserViewSet(ModelViewSet):
    """User View Set"""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
