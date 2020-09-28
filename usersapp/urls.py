from django.urls import path
from .views import *

urlpatterns = [
	path('signup/',customer_signup,name='signup'),
	path('login/',customer_login,name='login'),
	path('logout/',logout_view,name='logout'),
]