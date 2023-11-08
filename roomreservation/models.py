from django.db import models
from django.core.exceptions import ValidationError
from account.models import Account

# Create your models here.

class Room(models.Model):
    id = models.CharField(max_length=10, unique=True, primary_key=True)
    name = models.CharField(max_length=20)
    capacity = models.IntegerField()
    description = models.TextField()
    status = models.BooleanField(default=True)
    pic = models.ImageField(upload_to='room_pics', null=True, blank=True, default='room_pics/default.jpg')
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Reservation(models.Model):
    id = models.CharField(max_length=10, unique=True, primary_key=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    title = models.CharField(max_length=30, default="Reservation")
    description = models.TextField(null=True, blank=True)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)
    active = models.BooleanField(default=True)

    def clean(self):
        print('Start time: ', self.start_time, 'End time: ', self.end_time)
        if self.start_time >= self.end_time:
            raise ValidationError("End time must be after start time")

    def __str__(self):
        return self.title