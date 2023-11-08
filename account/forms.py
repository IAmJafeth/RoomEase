from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Account
from twiliosms.smsrequests import check_phone
class SignupForm(UserCreationForm):
	username = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
	email = forms.EmailField(max_length=254, required=True, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email', }))
	first_name = forms.CharField(max_length=30,required=True,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
	last_name = forms.CharField(max_length=30,required=True,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))
	password1 = forms.CharField(max_length=100, required=True, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
	password2 = forms.CharField(max_length=100, required=True, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2', 'first_name', 'last_name',)

class AccountForm(forms.ModelForm):
	phone = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}))

	class Meta:
		model = Account
		fields = ('phone',)

	def format_phone(self):
		# remove spaces and dashes
		phone = self.cleaned_data['phone']
		phone = phone.replace('-', '')
		phone = phone.replace(' ', '')
		phone = phone.replace('.', '')
		phone = phone.replace('(', '')
		phone = phone.replace(')', '')
		phone = phone.replace('+', '')
		return "+506"+phone
	
	def is_valid(self):
		valid = super(AccountForm, self).is_valid()
		if not valid:
			return valid

		phone = self.format_phone()
		print(phone)

		if len(phone) != 12:
			self.add_error('phone', 'Invalid phone number length')
			return False
		
		if not phone.replace('+', '').isdigit():
			self.add_error('phone', 'Invalid phone number characters')
			return False
		
		if not check_phone(phone):
			self.add_error('phone', 'Invalid phone number')
			return False
		
		return True

	def save(self, user, commit=True):
		account = super(AccountForm, self).save(commit=False)
		account.phone = self.format_phone()
		account.user = user
		if commit:
			account.save()
		return account

class LoginForm(AuthenticationForm):
	username = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
	password = forms.CharField(max_length=100, required=True, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
	remember_me = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}), required=False)