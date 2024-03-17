""" URLConf for lensverse.posts """

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from lensverse.posts.views import PostViewSet


# Create your URLConf here.
router = DefaultRouter(trailing_slash=False)
router.register("posts", PostViewSet, "pix")

sub_router = DefaultRouter()

urlpatterns = [
    path("", include(router.urls)),
    path("posts/<int:id>/", include((sub_router.urls, "posts"), namespace="posts")),
]
