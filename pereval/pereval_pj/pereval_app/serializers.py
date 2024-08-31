from .models import *
from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = [
            'winter', 'summer', 'autumn', 'spring'
                  ]


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = [
            'email', 'phone', 'fam', 'name', 'otc'
        ]


class CoordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coords
        fields = [
            'latitude', 'longitude', 'height'
        ]


class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = [
            'title_img', 'data'
        ]


class AddedSerializer(WritableNestedModelSerializer):
    add_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    user = UsersSerializer()
    coord = CoordsSerializer()
    level = LevelSerializer()
    images = ImagesSerializer(many=True)

    class Meta:
        model = Added
        fields = [
            'id', 'beautyTitle', 'title', 'other_titles', 'connect', 'add_time',
            'user', 'coord', 'level', 'activities_types', 'status', 'images'
        ]
