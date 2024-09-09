from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import *
from .models import *


class LevelViewSet(viewsets.ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer


class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer


class CoordsViewSet(viewsets.ModelViewSet):
    queryset = Coords.objects.all()
    serializer_class = CoordsSerializer


class ImagesViewSet(viewsets.ModelViewSet):
    queryset = Images.objects.all()
    serializer_class = ImagesSerializer


class AddedViewSet(viewsets.ModelViewSet):
    queryset = Added.objects.all()
    serializer_class = AddedSerializer
    filterset_fields = ['user__email',]
