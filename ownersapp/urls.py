from django.urls import path
from .views import *

urlpatterns = [
	path('',admin_home,name="admin-home"),
	path('myservices',myservices_view,name="myservices"),
	path('myservices/<int:id>/delete/',delete_service,name="delete-service"),
	path('myservices/<int:id>/edit/',edit_service,name="edit-service"),
	path('bookings/all/',allbookings,name="all-bookings"),
	path('bookings/<int:id>/edit',editbookings,name="edit-bookings"),
	path('staff/details/',staff_details_view,name="staff-details"),
	path('customer/details/',customer_details_view,name="customer-details"),
]