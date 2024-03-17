""" API endpoints for lensverse.posts """

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from lensverse.posts.models import Post
from lensverse.posts.serializers import PostSerializer


# Create your views here.
class PostViewSet(ModelViewSet):
    """Create, read, update and delete Posts"""

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    search_fields = []
    ordering_fields = []
    filterset_fields = []
