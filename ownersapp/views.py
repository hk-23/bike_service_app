from django.shortcuts import render,redirect
from .models import Service
from .forms import *
from datetime import datetime
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.contrib import messages
from usersapp.models import User
from usersapp.forms import SignupForm
from bookingsapp.models import Booking
from django.core.mail import send_mail
from usersapp.decorators import is_staff,is_admin

# Create your views here.
def home(request):
	return render(request,'home.html')

@is_staff
def admin_home(request):
	return render(request,'ownersapp/admin_home.html')

@is_staff
def myservices_view(request):
	myservices = Service.objects.all()
	myForm = AddServiceForm(request.POST or None)
	if myForm.is_valid():
		if request.user.user_type == 1:
			myForm.save()
		else:
			messages.info(request,'Staffs cannot Add a new Service. Only Admin Can Add New Service')
	context = {
		'form': myForm,
		'myservices': myservices,
	}
	return render(request,'ownersapp/myservices.html',context=context)

@is_staff
def edit_service(request,id):
	if request.method == "POST":
		name = request.POST.get('name')
		if Service.objects.filter(id=id).exists():
			Service.objects.filter(id=id).update(name=name)
		else:
			pass
		return redirect('myservices')
	else:
		return redirect('homepage')

@is_admin
def delete_service(request,id):
	serv = get_object_or_404(Service,id=id)
	serv.delete()
	messages.success(request,'Deleted Successfully!')
	return redirect('myservices')

@is_staff
def allbookings(request):
	book_obj = Booking.objects.all().order_by('booked_on').reverse()
	context = {
		'booking': book_obj,
	}
	return render(request,'ownersapp/bookings.html',context=context)

@is_staff
def editbookings(request,id):
	book_obj = get_object_or_404(Booking,id=id)
	myForm = BookingUpdateForm(request.POST or None,instance=book_obj,request=request)
	if myForm.is_valid():
		form_obj = myForm.save(commit=False)
		if request.POST.get('submit') == "ready":
			form_obj.status = "ready"
			form_obj.ready_by = User.objects.get(id=request.user.id)
			form_obj.save()
			send_ready_status_mail(id)
		elif request.POST.get('submit') == "delivered":
			form_obj.status = "delivered"
			form_obj.delivered_on = datetime.now()
			form_obj.delivered_by = User.objects.get(id=request.user.id)
			form_obj.save()
			send_delivered_status_mail(id)
		elif request.POST.get('submit') == "canceled":
			form_obj.status = "canceled"
			form_obj.canceled_by = User.objects.get(id=request.user.id)
			form_obj.save()
			send_canceled_status_mail(id)
		else:
			pass
	context = {
		'form': myForm,
		'booking': book_obj,
	}
	return render(request,'ownersapp/edit_bookings.html',context=context)

@is_staff
def staff_details_view(request):
	staff_obj = User.objects.filter(user_type=2)
	myForm = SignupForm(request.POST or None)
	context = {
		'staff': staff_obj,
		'form':  myForm,
	}
	return render(request,'ownersapp/staff_details.html',context=context)

@is_staff
def customer_details_view(request):
	customer_obj = User.objects.filter(user_type=3)
	context = {
		'customer': customer_obj,
	}
	return render(request,'ownersapp/customer_details.html',context=context)

def send_ready_status_mail(id):
	b = Booking.objects.get(id=id)
	msg = "Hey {},\n\nYour Bike Service for Vehicle No: {} is completed and its now Ready for Delivery.\n\n\
	The Total Amount is: {}\n\nRegards,\n\tHudson Sparklers."
	msg = msg.format(b.cid.get_full_name(),b.vehicle_no,b.amount)
	send_mail('Hudson Sparklers',msg,'no-reply@hudsonsparklers.in',[b.cid.email],)

def send_delivered_status_mail(id):
	b = Booking.objects.get(id=id)
	msg = "Hey {},\n\n\tYour Bike Service for Vehicle No: {} has been successfully Delivered.\n\n\
	The Total Amount Paid: {}/- \n\n\
	If you have any problems regarding the this service please feel free to contact us!\n\n\
	Regards,\n\tHudson Sparklers."
	msg = msg.format(b.cid.get_full_name(),b.vehicle_no,b.amount)
	send_mail('Hudson Sparklers',msg,'no-reply@hudsonsparklers.in',[b.cid.email],)

def send_canceled_status_mail(id):
	b = Booking.objects.get(id=id)
	msg = "Hey {},\n\n\tYour Bike Service for Vehicle No: {} is been canceled by our team.\n\n\
	We are sorry for this inconvenience caused.\n\n\
	To Know More about why it was canceled feel free to contact us!\n\n\
	Regards,\n\tHudson Sparklers."
	msg = msg.format(b.cid.get_full_name(),b.vehicle_no,b.amount)
	send_mail('Hudson Sparklers',msg,'no-reply@hudsonsparklers.in',[b.cid.email],)