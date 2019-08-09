from rest_framework import serializers
from django.contrib.auth.models import User

from chat_room.models import Room


class UserSerializer(serializers.ModelSerializer):
    """Сериализация юзера"""

    class Meta:
        model = User
        fields = ('id', 'username')


class RoomSrializers(serializers.ModelSerializer):
    """Сериализация комнаты чата"""

    creator = UserSerializer()
    invited = UserSerializer(many=True)

    class Meta:
        model = Room
        fields = ('creator', 'invited', 'creation_date')
