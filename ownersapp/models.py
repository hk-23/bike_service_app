from django.db import models
from usersapp.models import User

# Create your models here.

class Services(models.Model):
	name = models.CharField(max_length=30)