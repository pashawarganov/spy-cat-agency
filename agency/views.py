from django.shortcuts import render
from rest_framework import viewsets

from agency.models import Cat, Target, Mission
from agency.serializers import (
    CatSerializer,
    TargetSerializer,
    MissionSerializer
)


class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer


class TargetViewSet(viewsets.ModelViewSet):
    queryset = Target.objects.all()
    serializer_class = TargetSerializer


class MissionViewSet(viewsets.ModelViewSet):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer
