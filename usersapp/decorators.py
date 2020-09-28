from django.shortcuts import redirect
from django.contrib import messages
from .models import User

def is_customer(function):
	def wrap(request,*args,**kwargs):
		if request.user.is_authenticated:
			if request.user.user_type == 3:
				return function(request,*args,**kwargs)
			else:
				messages.info(request,'Please Login Using Customer Account')
				return redirect('login')
		else:
			messages.info(request,'Login To continue')
			return redirect('login')
	wrap.__doc__ = function.__doc__
	wrap.__name__ = function.__name__
	return wrap

def is_staff(function):
	def wrap(request,*args,**kwargs):
		if request.user.is_authenticated:
			if request.user.user_type == 2 and request.user.user_type ==1 :
				return function(request,*args,**kwargs)
			else:
				messages.info(request,'Please Login Using Staff Account')
				return redirect('login')
		else:
			messages.info(request,'Login To continue')
			return redirect('login')
	wrap.__doc__ = function.__doc__
	wrap.__name__ = function.__name__
	return wrap

def is_admin(function):
	def wrap(request,*args,**kwargs):
		if request.user.is_authenticated:
			if request.user.user_type == 1:
				return function(request,*args,**kwargs)
			else:
				messages.info(request,'Please Login Using Admin Account')
				return redirect('login')
		else:
			messages.info(request,'Login To continue')
			return redirect('login')
	wrap.__doc__ = function.__doc__
	wrap.__name__ = function.__name__
	return wrap