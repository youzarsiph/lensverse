""" URLConf for lensverse.profiles """

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from lensverse.profiles.views import ProfileViewSet


# Create your URLConf here.
router = DefaultRouter(trailing_slash=False)
router.register("profiles", ProfileViewSet, "post")

sub_router = DefaultRouter()

urlpatterns = [
    path("", include(router.urls)),
    path("profiles/<int:id>/", include(sub_router.urls)),
]
