from typing import Any
from django import forms
from django.contrib.auth.models import User
from .models import Account
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm



class SignupForm(UserCreationForm):
	username = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
	email = forms.EmailField(max_length=254, required=True, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
	password1 = forms.CharField(max_length=100, required=True, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
	password2 = forms.CharField(max_length=100, required=True, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2')


class LoginForm(AuthenticationForm):
	username = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
	password = forms.CharField(max_length=100, required=True, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
	remember_me = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}), required=False)