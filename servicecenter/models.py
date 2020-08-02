from django.db import models
from administrator.models import CarManufacturer,BikeManufacturer

# Create your models here.
class CarServiceCenter(models.Model):
	name=models.CharField(max_length=80)
	email=models.EmailField(max_length=30)
	address=models.TextField(max_length=100)
	phone=models.CharField(max_length=10)
	alt_phone=models.CharField(max_length=10)
	password=models.CharField(max_length=10)
	confirm_password=models.CharField(max_length=10)
	website=models.URLField(null=True,blank=True)
	opening_time=models.CharField(max_length=20)
	closing_time=models.CharField(max_length=20)
	manufacturer=models.ForeignKey(CarManufacturer,on_delete=models.CASCADE)
	createdat=models.DateTimeField(auto_now_add=True)
	updatedat=models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name
	
class BikeServiceCenter(models.Model):
	name=models.CharField(max_length=80)
	email=models.EmailField(max_length=30)
	address=models.TextField(max_length=100)
	phone=models.CharField(max_length=10)
	alt_phone=models.CharField(max_length=10)
	password = models.CharField(max_length=10)
	confirm_password = models.CharField(max_length=10)
	website=models.URLField(max_length=20)
	opening_time=models.CharField(max_length=20)
	closing_time=models.CharField(max_length=20)
	manufacturer=models.ForeignKey(BikeManufacturer,on_delete=models.CASCADE)
	createdat=models.DateTimeField(auto_now_add=True)
	updatedat=models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name

BOOKEDFOR =(('REPAIR','REPAIR'),('SERVICE','SERVICE'),('REPAIR AND SERVICE','REPAIR AND SERVICE'))
SERVICESTATUS =(('REQUEST BOOKING','REQUEST BOOKING'),('CANCELLED BY OWNER','CANCELLED BY OWNER'),('CANCELLED BY ADMIN','CANCELLED BY ADMIN'),('CONFIRM BY ADMIN','CONFIRM BY ADMIN'),('PICKED UP','PICKED UP'),('SERVICE STARTED','SERVICE STARTED'),('SERVICE COMPLETED','SERVICE COMPLETED'),('PAYMENT DONE','PAYMENT DONE'),('OUT FOR DELIVERY','OUT FOR DELIVERY'),('DELIVERED','DELIVERED'),('CANCELLED BY ADMIN ON OWNERS REQUEST','CANCELLED BY ADMIN ON OWNERS REQUEST'))

class CarServiceRequest(models.Model):
	carservicecenter = models.ForeignKey(CarServiceCenter, on_delete=models.CASCADE)
	vehicle_no = models.CharField(max_length=40)
	owned_by = models.EmailField(null=True, blank=True)
	bookdate   = models.DateField()
	bookedfor  = models.CharField(max_length=40, choices=BOOKEDFOR)
	estimatedcost = models.IntegerField(null=True,blank=True)
	actualcost = models.IntegerField(null=True, blank=True)
	description= models.TextField()
	servicestatus = models.CharField(max_length=30, choices=SERVICESTATUS,default='REQUEST BOOKING')

class BikeServiceRequest(models.Model):
	bikeservicecenter = models.ForeignKey(BikeServiceCenter, on_delete=models.CASCADE)
	vehicle_no = models.CharField(max_length=40)
	owned_by = models.EmailField(null=True,blank=True)
	bookdate   = models.DateField()
	bookedfor  = models.CharField(max_length=40, choices=BOOKEDFOR)
	estimatedcost = models.IntegerField(null=True,blank=True)
	actualcost = models.IntegerField(null=True, blank=True)
	description= models.TextField()
	servicestatus = models.CharField(max_length=30, choices=SERVICESTATUS,default='REQUEST BOOKING')

