from django.db import models

from django.contrib.auth.models import User


class Room(models.Model):
    """ Модель комнаты чата """

    creator = models.ForeignKey(User, verbose_name="Создатель", on_delete=models.CASCADE)
    room_name = models.TextField("Название комнаты", max_length=20)
    invited = models.ManyToManyField(User, verbose_name="Участники", related_name="invited_user")
    creation_date = models.DateTimeField("Дата создания комнаты", auto_now_add=True)

    class Meta:
        verbose_name = "Комната чата"
        verbose_name_plural = "Комната чата"
        
    
class Chat(models.Model):
    """ Модель чата """
    
    room = models.ForeignKey(Room, verbose_name="Комната чата", on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)
    text = models.TextField("Сообщение", max_length=500)
    send_date = models.DateTimeField("Дата отправки сообщения", auto_now_add=True)
    
    class Meta:
        verbose_name = 'Сообщения в чате'
        verbose_name_plural = 'Сообщения в чате'
