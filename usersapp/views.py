from django.shortcuts import render, redirect
from .models import User
from .forms import SignupForm,LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password

# Create your views here.

def customer_signup(request):
	myForm = SignupForm(request.POST or None)
	if myForm.is_valid():
		user_obj = myForm.save(commit=False)
		user_obj.password = make_password(user_obj.password)
		user_obj.user_type = 3
		user_obj.save()
	context = {
		'form':myForm,
	}
	return render(request,'usersapp/customer_signup.html',context=context)

def customer_login(request):
	myForm = LoginForm(request.POST or None)
	if myForm.is_valid():
		email = myForm.cleaned_data.get('email')
		password = myForm.cleaned_data.get('password')
		user = authenticate(request,email=email,password=password)
		if user is not None:
			login(request,user)
			messages.success(request,"Loged In successfully!")
			if user.user_type in (1,2):
				return redirect('admin_home')
			elif user.user_type == 3:
				return redirect('homepage')
			return redirect('homepage')
		else:
			messages.error(request,"Invalid username or password!")
	context = {
		'form': myForm,
	}
	return render(request,'usersapp/customer_login.html',context=context)

def logout_view(request):
	logout(request)
	return redirect('homepage')