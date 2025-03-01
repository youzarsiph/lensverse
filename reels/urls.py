""" URLConf for lensverse.reels """

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from lensverse.reels.views import StoryViewSet


# Create your URLConf here.
router = DefaultRouter(trailing_slash=False)
router.register("stories", StoryViewSet, "story")

sub_router = DefaultRouter()

urlpatterns = [
    path("", include(router.urls)),
    path("stories/<int:id>/", include(sub_router.urls)),
]
