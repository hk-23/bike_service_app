from django import forms
from .models import Services

class AddServiceForm(forms.ModelForm):
	class Meta:
		model = Services
		fields = ['name']