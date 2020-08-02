from django.db import models
from administrator.models import CarManufacturer,BikeManufacturer
# Create your models here.
GENDER_CHOICE=(('MALE','MALE'),('FEMALE','FEMALE'),('OTHER','OTHER'))
CITY_CHOICE=(('Bhopal','Bhopal'),('Gwalior','Gwalior'),('Indore','Indore'),('Chhatarpur','Chhatarpur'),('Other','Other'))
class Register(models.Model):
	name=models.CharField(max_length=50)
	email=models.EmailField(max_length=35,unique=True)
	phone=models.CharField(max_length=10,unique=True)
	alt_phone=models.CharField(max_length=10,unique=True)
	password=models.CharField(max_length=15)
	confirm_password=models.CharField(max_length=10)
	gender=models.CharField(max_length=7,choices=GENDER_CHOICE)
	home_address=models.CharField(max_length=1024)
	vehicle_delivery_address=models.CharField(max_length=1024)
	city=models.CharField(max_length=30,choices=CITY_CHOICE)

	def __str__(self):
		return self.email


class CarVehicle(models.Model):
	vehicle_no=models.CharField(max_length=15,unique=True)
	manufacturer_name=models.ForeignKey(CarManufacturer,on_delete=models.CASCADE)
	vehicle_type=models.CharField(max_length=15,default='CAR')
	model_name=models.CharField(max_length=20)
	owned_by=models.EmailField()
	createdat=models.DateTimeField(auto_now_add=True,null=True,blank=True)
	#carimage = models.ImageField(null=True,blank=True)
	updatedat=models.DateTimeField(auto_now=True,null=True,blank=True)

class BikeVehicle(models.Model):
	vehicle_no=models.CharField(max_length=15,unique=True)
	manufacturer_name=models.ForeignKey(BikeManufacturer,on_delete=models.CASCADE)
	vehicle_type=models.CharField(max_length=15,default='BIKE')
	model_name=models.CharField(max_length=20)
	owned_by=models.EmailField()
	createdat=models.DateTimeField(auto_now_add=True,null=True,blank=True)
	updatedat=models.DateTimeField(auto_now=True,null=True,blank=True)
