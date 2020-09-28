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
	class Meta:
		model = Booking
		fields = ['brand','services','service_on']

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