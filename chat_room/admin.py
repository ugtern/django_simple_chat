from django.contrib import admin
from chat_room.models import Room, Chat


class RoomAdmin(admin.ModelAdmin):
    """ Админ панель комант чата """

    list_display = ('creator', 'invited_user', 'creation_date')

    def invited_user(self, obj):
        return '\n'.join([user.username for user in obj.invited.all()])


class ChatAdmin(admin.ModelAdmin):
    """ Админка диалогов """

    list_display = ('room', 'user', 'text', 'send_date')

admin.site.register(Room, RoomAdmin)
admin.site.register(Chat, ChatAdmin)
