from django.urls import path
from .views import *

urlpatterns = [
	path('',BookingView,name="book-a-service"),
	path('mybookings/',MyBookings,name="mybookings"),
]