from django.contrib import admin

from servicecenter.models import CarServiceRequest, BikeServiceRequest
from .models import Register,BikeVehicle,CarVehicle


# Register your models here.
admin.site.register(Register)
admin.site.register(BikeVehicle)
admin.site.register(CarVehicle)
admin.site.register(CarServiceRequest)
admin.site.register(BikeServiceRequest)

