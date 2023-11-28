from django.db import models
from django.contrib.auth.models import User


class SoftDelete(models.Model):
    deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True

    def delete(self):
        self.deleted = True
        self.save()

class Account(SoftDelete):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, null=True, blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', null=True, blank=True, default='profile_pics/default.png')

    def __str__(self) -> str:
        return self.user.username

    def delete(self):
        self.profile_pic.delete()
        self.profile_pic = 'profile_pics/deleted.png'
        super().delete()