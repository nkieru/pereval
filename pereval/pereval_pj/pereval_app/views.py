from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import viewsets, generics
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

    def partial_update(self, request, *args, **kwargs):
        added = self.get_object()
        if added.status == 'N':
            serializer = AddedSerializer(added, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {
                        'state': '1',
                        'message': 'Changes saved',
                    }
                )
            else:
                return Response(
                    {
                        'state': '0',
                        'message': serializer.errors
                    }
                )
        else:
            return Response(
                {
                    'state': '0',
                    'message': f'Changes rejected. Status: {added.get_status_display()}'
                }
            )


class AddedFromEmailView(generics.ListAPIView):
    serializer_class = AddedSerializer

    def get(self, request, *args, **kwargs):
        email = kwargs.get('email', None)
        if Added.objects.filter(user__email=email):
            added_from_email = AddedSerializer(Added.objects.filter(user__email=email), many=True).data
        else:
            added_from_email = {'message': f'User with email {email} does not exist'}
        return JsonResponse(added_from_email, safe=False)
