""" URLConf for pixhub.pixes """


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from pixhub.pixes.views import PixViewSet


# Create your URLConf here.
router = DefaultRouter(trailing_slash=False)
router.register("pixes", PixViewSet, "pix")

sub_router = DefaultRouter()

urlpatterns = [
    path("", include(router.urls)),
    path("pixes/<int:id>/", include((sub_router.urls, "pixes"), namespace="pixes")),
]
