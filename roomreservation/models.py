from django.db import models
from account.models import Account

# Create your models here.

class Room(models.Model):
    room_id = models.CharField(max_length=10, unique=True, primary_key=True)
    room_name = models.CharField(max_length=20)
    room_capacity = models.IntegerField()
    room_description = models.TextField()
    room_status = models.BooleanField(default=True)
    room_pic = models.ImageField(upload_to='room_pics', null=True, blank=True, default='room_pics/default.jpg')
    active = models.BooleanField(default=True)

class Reservation(models.Model):
    reservation_id = models.CharField(max_length=10, unique=True, primary_key=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    reservation_date = models.DateField()
    reservation_start_time = models.TimeField()
    reservation_end_time = models.TimeField()
    reservation_description = models.TextField(null=True, blank=True)
    reservation_status = models.BooleanField(default=True)
    active = models.BooleanField(default=True)