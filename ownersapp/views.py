from django.shortcuts import render,redirect
from .models import Service
from .forms import *

# Create your views here.
def home(request):
	return render(request,'home.html')

def admin_home(request):
	return render(request,'ownersapp/admin_home.html')

def myservices_view(request):
	myservices = Service.objects.all()
	myForm = AddServiceForm(request.POST or None)
	if myForm.is_valid():
		print('its valid')
	context = {
		'form': myForm,
		'myservices': myservices,
	}
	return render(request,'ownersapp/myservices.html',context=context)