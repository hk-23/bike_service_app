from django.db import models

from django.core.mail import send_mail
from django.contrib.auth.models import AbstractUser,BaseUserManager
from django.contrib.auth.base_user import AbstractBaseUser

class UserManager(BaseUserManager):
	use_in_migrations = True

	def _create_user(self,email,password,**extra_fields):
		if not email:
			raise ValueError("The email is required!")
		email = self.normalize_email(email)
		user = self.model(email=email,**extra_fields)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_user(self,email,password=None,**extra_fields):
		extra_fields.setdefault('is_staff',False)
		extra_fields.setdefault('is_superuser',False)
		return self._create_user(email,password,**extra_fields)

	def create_superuser(self,email,password,**extra_fields):
		extra_fields.setdefault('is_staff',True)
		extra_fields.setdefault('is_superuser',True)

		if extra_fields.get('is_staff') is not True:
			raise ValueError('Superuser must have is_staff=True')
		if extra_fields.get('is_superuser') is not True:
			raise ValueError('Superuser must have is_superuser=True')

		return self._create_user(email,password,**extra_fields)

# Create your models here.
class User(AbstractUser):
	username = None
	email = models.EmailField(unique=True)
	first_name = models.CharField(max_length=35)
	mobile = models.CharField(unique=True,max_length=10)
	user_type_choice = ((1,'Owner'),(2,'Customer'))
	user_type = models.PositiveSmallIntegerField(choices=user_type_choice)

	objects = UserManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []

