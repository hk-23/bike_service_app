import re
from datetime import date,datetime
from django import forms
from .models import Booking
from ownersapp.models import Service

class BookingForm(forms.ModelForm):
	services = forms.ModelMultipleChoiceField(
		widget=forms.CheckboxSelectMultiple,
		queryset=Service.objects.all(),
	)
	service_on = forms.DateField(widget=forms.TextInput(attrs={'type':'date'}))
	vehicle_no = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "TN-37-AA-1234"}))
	class Meta:
		model = Booking
		fields = ['brand','vehicle_no','services','service_on']

	def clean_vehicle_no(self):
		vehicle_no = self.cleaned_data.get('vehicle_no').upper()
		if not re.match("[A-Z]{2}-[0-9]{1,2}-[A-Z]{1,2}-[0-9]{1,4}$",vehicle_no):
			raise forms.ValidationError('Please Enter in the correct format. Ex: TN-37-AA-1234')
		return vehicle_no

	def clean_service_on(self):
		service_on = self.cleaned_data.get('service_on')
		diff = service_on - date.today()
		diff = diff.days
		if service_on == date.today() and datetime.now().hour>18:
			raise forms.ValidationError('Sorry! Bookings closed for today. Try for Tomorrow.')
		if diff<0:
			raise forms.ValidationError('Please Enter a Valid Date!')
		if diff>90:
			raise forms.ValidationError('Bookings are allowed only 3 months prior')
		return service_on