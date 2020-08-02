from django.db import models


# Create your models here.

class CarManufacturer(models.Model):
	 manufacturer_name = models.CharField(max_length = 30,unique=True)
	
	 def __str__(self):
	 	 return self.manufacturer_name

class BikeManufacturer(models.Model):
	manufacturer_name = models.CharField(max_length = 30,unique = True)
	
	def __str__(self):
		return self.manufacturer_name



