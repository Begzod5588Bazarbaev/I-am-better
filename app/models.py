from django.db import models

from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.CharField(max_length=45, verbose_name='Имя')
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Человек'

class Calendar(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=45, verbose_name='Имя')
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Календарь'

class Event(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    calendarId = models.ForeignKey(Calendar, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, verbose_name='Название')
    location = models.CharField(max_length=200, verbose_name='Локация')
    start = models.DateTimeField(verbose_name='Начало')
    end = models.DateTimeField(verbose_name='Конец')
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Праздник'

class Invites(models.Model):
    user_id = models.ForeignKey('User',on_delete=models.CASCADE,)
    eventId = models.ForeignKey('Event',on_delete=models.CASCADE,)

    class Meta:
        verbose_name_plural = 'Приглашение'