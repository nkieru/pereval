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

    def save(self, **kwargs):
        self.is_valid()
        user = Users.objects.filter(email=self.validated_data.get('email'))
        if user.exists():
            return user.first()
        else:
            user_create = Users.objects.create(
                email=self.validated_data.get('email'),
                phone=self.validated_data.get('phone'),
                fam=self.validated_data.get('fam'),
                name=self.validated_data.get('name'),
                otc=self.validated_data.get('otc'),
            )
            return user_create


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

    def validate(self, fields):
        if self.instance is not None:
            user = self.instance.user
            user_fields = fields.get('user')
            fields_changes = [
                user.fam != user_fields['fam'],
                user.name != user_fields['name'],
                user.otc != user_fields['otc'],
                user.phone != user_fields['phone'],
                user.email != user_fields['email'],
            ]
            if user_fields is not None and any(fields_changes):
                raise serializers.ValidationError(
                    {
                        'You cannot change user data'
                    }
                )
        return fields
