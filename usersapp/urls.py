from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
	path('signup/',customer_signup,name='signup'),
	path('login/',login,name='login'),
	path('logout/',logout_view,name='logout'),
	path('profile/',profile_view,name='profile'),
	path('staff/signup',staff_signup,name='staff_signup'),
	# path('change-password/', auth_views.PasswordChangeView.as_view(),name="password_change"),
	# path('reset-password/', auth_views.PasswordResetView.as_view(),name="password_reset"),
	# path('reset-password/done', auth_views.PasswordResetDoneView.as_view(),name="password_reset_done"),
	# path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(),name="password_reset_confirm"),
	# path('reset/complete', auth_views.PasswordResetCompleteView.as_view(),name="password_reset_complete"),
]