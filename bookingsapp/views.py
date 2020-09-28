from django.shortcuts import render
from .forms import *
from usersapp.models import User
from usersapp.decorators import *
# from django.contrib.auth.decorators import login_required

# Create your views here.
@is_customer
def BookingView(request):
	myForm = BookingForm(request.POST or None)
	if myForm.is_valid():
		book_obj = myForm.save(commit=False)
		book_obj.cid = User.objects.get(id=request.user.id)
		book_obj.save()
		myForm.save_m2m()
	context = {
		'form': myForm,
	}
	return render(request,'bookingsapp/book.html',context=context)