from django.urls import path, include
from rest_framework import routers

from agency.views import (
    CatViewSet,
    TargetViewSet,
    MissionViewSet
)

app_name = "agency"

router = routers.DefaultRouter()
router.register("cats", CatViewSet)
router.register("missions", MissionViewSet)

urlpatterns = [path("", include(router.urls))]
