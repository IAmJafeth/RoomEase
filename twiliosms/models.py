from django.db import models


class SoftDelete(models.Model):
    deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True

    def delete(self):
        self.deleted = True
        self.save()

class TwilioAccount(SoftDelete):
    account_sid = models.CharField(max_length=100)
    auth_token = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    selected = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.account_sid
    
