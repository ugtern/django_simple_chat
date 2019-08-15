from rest_framework import serializers
from django.contrib.auth.models import User

from chat_room.models import Room, Chat


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
        fields = ('id', 'creator', 'invited', 'creation_date', 'room_name')


class ChatSerializers(serializers.ModelSerializer):
    """ Сериализация чата """

    user = UserSerializer()

    class Meta:
        model = Chat
        fields = ('user', 'text', 'send_date')


class ChatPostSerializers(serializers.ModelSerializer):
    """ Сериализация чата """

    class Meta:
        model = Chat
        fields = ('room', 'text')