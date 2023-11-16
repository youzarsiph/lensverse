""" URLConf for pixhub.topics """


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from pixhub.topics.views import TopicViewSet


# Create your URLConf here.
router = DefaultRouter(trailing_slash=False)
router.register("topics", TopicViewSet, "topic")

sub_router = DefaultRouter()

urlpatterns = [
    path("", include(router.urls)),
    path("topics/<int:id>/", include((sub_router.urls, "topics"), namespace="topics")),
]
