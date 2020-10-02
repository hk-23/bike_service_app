from django.shortcuts import render,redirect
from .forms import *
from usersapp.models import User
from usersapp.decorators import *
from django.contrib import messages
from django.core.mail import send_mail
# from django.contrib.auth.decorators import login_required

# Create your views here.
@is_customer
def BookingView(request):
	myForm = BookingForm(request.POST or None)
	print('its working')
	if myForm.is_valid():
		print('itsvalid')
		book_obj = myForm.save(commit=False)
		book_obj.cid = User.objects.get(id=request.user.id)
		book_obj.save()
		myForm.save_m2m()
		messages.success(request,"Booking Successfully Completed")
		send_mail_to_admin();
		return redirect('mybookings')
	context = {
		'form': myForm,
	}
	return render(request,'bookingsapp/book.html',context=context)

@is_customer
def MyBookings(request):
	book_obj = Booking.objects.filter(cid=request.user.id).order_by('booked_on').reverse()
	context = {
		'booking': book_obj,
	}
	return render(request,'bookingsapp/mybookings.html',context=context)

def send_mail_to_admin():
	user_obj = User.objects.filter(user_type=1)
	for u in user_obj:
		msg_plain = "Hey {},\n\t A New Booking have been made by one of your users.\nTo know more about the booking details visit your Admin Page!\n\n\
		".format(str(u.get_full_name()))
		send_mail(
			'New Booking Alert',
			msg_plain,
			'no-reply@hudsonsparklers.in',
			[u.email],
			fail_silently = True,
		)