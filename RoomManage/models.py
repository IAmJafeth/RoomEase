from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Room(models.Model):
    room_id = models.CharField(max_length=10, unique=True, primary_key=True)
    room_name = models.CharField(max_length=20)
    room_capacity = models.IntegerField()
    room_description = models.TextField()
    room_status = models.BooleanField(default=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.room_name
    
class Reservation(models.Model):
    reservation_id = models.CharField(max_length=10, unique=True, primary_key=True)
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    reservation_date = models.DateField()
    reservation_start_time = models.TimeField()
    reservation_end_time = models.TimeField()
    reservation_description = models.TextField()
    reservation_status = models.BooleanField(default=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.reservation_id
    


