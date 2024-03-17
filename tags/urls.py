""" URLConf for lensverse.tags """

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from lensverse.tags.views import TagViewSet


# Create your URLConf here.
router = DefaultRouter(trailing_slash=False)
router.register("tags", TagViewSet, "topic")

sub_router = DefaultRouter()

urlpatterns = [
    path("", include(router.urls)),
    path("tags/<int:id>/", include((sub_router.urls, "tags"), namespace="tags")),
]
