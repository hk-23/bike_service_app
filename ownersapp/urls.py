from django.urls import path
from .views import *

urlpatterns = [
	path('home',admin_home,name="admin_home"),
	path('myservices',myservices_view,name="myservices"),
]