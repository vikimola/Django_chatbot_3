from django.db import models
import datetime
from django.utils import timezone


# Create your models here.
class Room(models.Model):
    room_name = models.CharField(max_length=500)


naive_time = datetime.datetime.utcnow()
aware_time = timezone.make_aware(naive_time)


class Message(models.Model):
    room_name = models.CharField(max_length=500)
    username = models.CharField(max_length=500)
    contents = models.CharField(max_length=500000000)
    timestamp = models.DateTimeField(default=timezone.now, blank=True)


class Users(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
