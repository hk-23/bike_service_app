from django import forms
from .models import Service

class AddServiceForm(forms.ModelForm):
	class Meta:
		model = Service
		fields = ['name']