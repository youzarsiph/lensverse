""" URLConf for lensverse.followers """

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from lensverse.followers.views import FollowerViewSet


# Create your URLConf here.
router = DefaultRouter(trailing_slash=False)
router.register("followers", FollowerViewSet, "follower")

sub_router = DefaultRouter()

urlpatterns = [
    path("", include(router.urls)),
]
