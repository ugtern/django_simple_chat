from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from django.contrib.auth.models import User

from chat_room.models import Room, Chat
from chat_room.seriallizers import RoomSrializers, ChatSerializers, ChatPostSerializers, UserSerializer


class Rooms(APIView):
    """ Комнаты чата """

    def get(self, request):
        rooms = Room.objects.all()
        serializer = RoomSrializers(rooms, many=True)
        return Response({'data': serializer.data})


class Dialogs(APIView):
    """ Диалоги чата """
    permission_classes = [permissions.IsAuthenticated]
    # permission_classes = [permissions.AllowAny]

    def get(self, request):
        room = request.GET.get('room')
        chat = Chat.objects.filter(room=room)
        serializer = ChatSerializers(chat, many=True)
        return Response({'data': serializer.data})

    def post(self, request):
        # room = request.data.get('room')
        dialog = ChatPostSerializers(data=request.data)
        if dialog.is_valid():
            dialog.save(user=request.user)
            return Response(status=201)
        else:
            return Response(status=400)


class ShowUsers(APIView):

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response({'data': serializer.data})

    def post(self, request):
        room = request.data.get('room')
        user = request.data.get('user')
        try:
            room = Room.objects.get(id=room)
            room.invited.add(user)
            room.save()
            return Response(status=201)
        except:
            return Response(status=400)