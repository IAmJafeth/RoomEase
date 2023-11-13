from django.db import models

class TwilioAccount(models.Model):
    account_sid = models.CharField(max_length=100)
    auth_token = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    selected = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return self.account_sid
    
