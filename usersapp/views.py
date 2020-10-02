from django.shortcuts import render, redirect
from .models import User
from .forms import SignupForm,LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from .decorators import is_admin

# Create your views here.

def customer_signup(request):
	myForm = SignupForm(request.POST or None)
	if myForm.is_valid():
		user_obj = myForm.save(commit=False)
		user_obj.password = make_password(user_obj.password)
		user_obj.user_type = 3
		user_obj.save()
		return redirect('login')
	context = {
		'form':myForm,
	}
	return render(request,'usersapp/customer_signup.html',context=context)

def customer_login(request):
	if request.user.is_authenticated:
		return redirect('homepage')
	myForm = LoginForm(request.POST or None)
	if myForm.is_valid():
		email = myForm.cleaned_data.get('email')
		password = myForm.cleaned_data.get('password')
		next_url = request.GET.get('next',None)
		print(next_url)
		user = authenticate(request,email=email,password=password)
		if user is not None:
			login(request,user)
			# messages.success(request,"Loged In successfully!")
			if user.user_type in (1,2):
				if next_url:
					return redirect(next_url)
				else:
					return redirect('admin_home')
			elif user.user_type == 3:
				if next_url:
					return redirect(next_url)
				else:
					return redirect('homepage')
			return redirect('homepage')
		else:
			messages.error(request,"Invalid username or password!")
	context = {
		'form': myForm,
	}
	return render(request,'usersapp/customer_login.html',context=context)

@is_admin
def staff_signup(request):
	myForm = SignupForm(request.POST or None)
	if myForm.is_valid():
		user_obj = myForm.save(commit=False)
		user_obj.password = make_password(user_obj.password)
		user_obj.user_type = 2
		user_obj.save()
		return redirect('staff-details')
	staff_obj = User.objects.filter(user_type=2)
	context = {'form': myForm,'staff': staff_obj,}
	return render(request,'ownersapp/staff_details.html',context=context)

def logout_view(request):
	logout(request)
	return redirect('homepage')