from django import forms
from .models import Service
from bookingsapp.models import Booking

class AddServiceForm(forms.ModelForm):
	class Meta:
		model = Service
		fields = ['name']

class BookingUpdateForm(forms.ModelForm):
	class Meta:
		model = Booking
		fields = ['amount']

	def __init__(self, *args, **kwargs):
		self.request = kwargs.pop('request', None)
		super(BookingUpdateForm, self).__init__(*args, **kwargs)

	def clean_amount(self):
		amt = self.cleaned_data.get('amount')
		status = self.request.POST.get('submit')
		if status in ("ready","delivered") and not amt:
			raise forms.ValidationError('This Field is required')
		return amt