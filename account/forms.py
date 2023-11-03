from django import forms
from django.contrib.auth.models import User
from .models import Account


def AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'city', 'country', 'image']