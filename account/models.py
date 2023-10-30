from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, null=True, blank=True)
    # profile_pic = models.ImageField(upload_to='profile_pics', null=True, blank=True, default='profile_pics/default.png')
    active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.user.username