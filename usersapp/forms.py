from django import forms
from .models import User

class SignupForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Retype Password'}))
	class Meta:
		model = User
		fields = ['email','first_name','last_name','mobile','password','confirm_password']

	#validating the email
	def clean_email(self):
		email = self.cleaned_data.get('email').lower()
		return email

	#validating the mobile no
	def clean_mobile(self):
		mobile = self.cleaned_data.get('mobile')
		if not len(mobile)==10:
			raise forms.ValidationError('Enter a valid Mobile Number')
		return mobile

	#validating the password
	def clean_password(self):
		password = self.cleaned_data.get('password')
		upper=lower=num=0
		for i in password:
			if i.isupper():upper+=1
			elif i.islower():lower+=1
			elif i.isnumeric():num+=1
		if not len(password)>=6:
			raise forms.ValidationError('Password Must be atleast 6 characters')
		if not upper:
			raise forms.ValidationError('Password Must have atleast 1 uppercase')
		if not lower:
			raise forms.ValidationError('Password Must have atleast 1 lowercase')
		if not num:
			raise forms.ValidationError('Password Must have atleast 1 numeric')
		return password

	#validating the confirm password field
	def clean_confirm_password(self):
		c_pass = self.cleaned_data.get('confirm_password')
		if not c_pass == self.cleaned_data.get('password'):
			raise forms.ValidationError('Password did not match')
		return c_pass

class LoginForm(forms.Form):
	email = forms.CharField(widget=forms.EmailInput())
	password = forms.CharField(widget=forms.PasswordInput())

class ProfileEditForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['first_name','last_name','email','mobile']

	#validating the email
	def clean_email(self):
		email = self.cleaned_data.get('email').lower()
		return email

	#validating the mobile no
	def clean_mobile(self):
		mobile = self.cleaned_data.get('mobile')
		if not len(mobile)==10:
			raise forms.ValidationError('Enter a valid Mobile Number')
		return mobile