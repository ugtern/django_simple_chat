from django.urls import path
from chat_room.views import Rooms, Dialogs, ShowUsers

urlpatterns = [
    path('room/', Rooms.as_view()),
    path('dialog/', Dialogs.as_view()),
    path('users/', ShowUsers.as_view()),
]
