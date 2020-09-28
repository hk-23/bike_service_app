from django.db import models
from usersapp.models import User

# Create your models here.

class Service(models.Model):
	name = models.CharField(max_length=30)

	def __str__(self):
		return self.name

# General service
# Oil change
# Electrical issues
# Clutch and brakes issues
# Engine / silencer noise issues
# Chain and sprocket Issues
# Filter change
# Re-painting / scratch removal
# Tyre puncture / replacement