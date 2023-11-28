from django.db import models
from django.core.exceptions import ValidationError
from account.models import Account
from django.utils import timezone

# Create your models here.

class SoftDelete(models.Model):
    deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True

    def delete(self):
        self.deleted = True
        self.save()

class Room(SoftDelete):
    name = models.CharField(max_length=20)
    capacity = models.IntegerField()
    description = models.TextField()
    status = models.BooleanField(default=True)
    pic = models.ImageField(upload_to='room_pics', null=True, blank=True, default='room_pics/default.png')

    def __str__(self):
        return self.name
    
    def delete(self):
        self.pic.delete()
        self.pic = 'room_pics/deleted.png'
        super().delete()

class Reservation(SoftDelete):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    description = models.TextField(null=True, blank=True)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    created_at = models.DateTimeField(default=timezone.localtime().now())
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    