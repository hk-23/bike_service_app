from django.db import models
from ownersapp.models import Service

# Create your models here.

brand_choice = (('aprila','Aprila'),('bajaj','Bajaj'),('harley-davidson','Harley-Davidson'),
	('hero','Hero'),('honda','Honda'),('ktm','KTM'),('mahindra','Mahindra'),('royal enfield','Royal Enfield'),
	('suzuki','Suzuki'),('tvs','TVS'),('vespa','Vespa'),('yamaha','Yamaha'))

class Booking(models.Model):
	cid = models.ForeignKey('usersapp.User',on_delete=models.CASCADE,related_name="cid")
	brand = models.CharField(max_length=30,choices=brand_choice)
	vehicle_no = models.CharField(max_length=15)
	services = models.ManyToManyField(Service)
	service_on = models.DateField()
	status_choice = (('pending','Pending'),('canceled','Canceled'),('ready','Ready'),('delivered','Delivered'))
	status = models.CharField(max_length=15,choices=status_choice,default=status_choice[0][0])
	amount = models.PositiveIntegerField(null=True,blank=True)
	booked_on = models.DateTimeField(auto_now_add=True)
	delivered_on = models.DateTimeField(null=True,blank=True)
	canceled_by = models.ForeignKey('usersapp.User',on_delete=models.CASCADE,related_name='canceled_by',null=True,blank=True)
	ready_by = models.ForeignKey('usersapp.User',on_delete=models.CASCADE,related_name='ready_by',null=True,blank=True)
	delivered_by = models.ForeignKey('usersapp.User',on_delete=models.CASCADE,related_name='delivered_by',null=True,blank=True)