from django.shortcuts import render, redirect
from django.http import HttpResponse

from customer.models import Register
from servicecenter.models import CarServiceCenter, BikeServiceCenter, CarServiceRequest, BikeServiceRequest
from.forms import CarServiceRegistrationForm,BikeServiceRegistrationForm,CarLoginForm,BikeLoginForm
from administrator.models import CarManufacturer,BikeManufacturer



# Create your views here.
def servicecenters_home(request):
	 carmanus=CarManufacturer.objects.all()
	 bikemanus=BikeManufacturer.objects.all()
	 context={'carmanus':carmanus,'bikemanus':bikemanus}
	 return render(request,'servicecenter/servicecenters_home.html',context)


def car_servicecenter_register_form(request):
	form=CarServiceRegistrationForm(request.POST or None)
	if request.method=="POST":
		if form.is_valid():
			try:
				form.save()
				return redirect('/servicecenter/car_service_center_login')
			except:
				return redirect('/servicecenter/car_servicecenter_register_form')
	context={'form':form}
	return render(request,'servicecenter/carserviceregistration.html',context)

def bike_servicecenter_register_form(request):
	form=BikeServiceRegistrationForm(request.POST or None)
	if request.method=="POST":
		if form.is_valid():
			try:
				form.save()
				return redirect('/bikeservicecenter/bike_service_center_login')
			except:
				return redirect('/servicecenter/bike_servicecenter_register_form')
	context={'form':form}
	return render(request,'servicecenter/bikeserviceregistration.html',context)

def car_service_center_login(request):
	form=CarLoginForm(request.POST or None)
	if request.method=="POST":
		if form.is_valid():
			username=form.cleaned_data.get('username')
			password=form.cleaned_data.get('password')
			try:
				user=CarServiceCenter.objects.get(email=username,password=password)
				request.session['username'] = user.email
				return redirect('/servicecenter/dashboard')
			except:
				return HttpResponse("<p> Sorry, Login failed</p>")

	context={'form':form}
	return render(request,'servicecenter/login_carservicecenter.html',context)


def bike_service_center_login(request):
	form=BikeLoginForm(request.POST or None)
	if request.method=="POST":
		if form.is_valid():
			username=form.cleaned_data.get('username')
			password=form.cleaned_data.get('password')
			try:
				user=BikeServiceCenter.objects.get(email=username,password=password)
				request.session['username'] = user.email
				return redirect('/servicecenter/dashboard')
			except:
				return HttpResponse("<p> Sorry, Login failed</p>")

	context={'form':form}
	return render(request,'servicecenter/login_bikeservicecenter.html',context)

def dashboard(request):

	return render(request,'servicecenter/dashboard.html')

def newbooking(request):
	cars = CarServiceRequest.objects.filter(servicestatus = 'REQUEST BOOKING')
	context = {'cars':cars}

	return render(request,'servicecenter/carbookingstatus.html',context)

def newbookingbike(request):
	bikes = BikeServiceRequest.objects.filter(servicestatus = 'REQUEST BOOKING')
	context = {'bikes':bikes}

	return render(request,'servicecenter/bikebookingstatus.html',context)

def costestimation(request,id):

	if request.method=='POST':
		car = CarServiceRequest.objects.get(id=id)
		estimatedcost = request.POST.get("estimatedcost")
		actualcost = request.POST.get("actualcost")
		car.estimatedcost = estimatedcost
		car.actualcost = actualcost
		car.servicestatus = 'CONFIRM BY ADMIN'
		car.save()
	context = {'id':id}

	return render(request,'servicecenter/costestimation.html',context)

def changestatuscar(request,id,servicestatus):
	booking = CarServiceRequest.objects.get(id = id)
	booking.servicestatus = servicestatus
	booking.save()
	print(servicestatus)
	return  HttpResponse ('<h3> Booking status is changed to '+servicestatus+' </h3>')




def confirmcar(request):
	cars = CarServiceRequest.objects.filter(servicestatus = 'CONFIRM BY ADMIN')
	context = {'cars':cars}

	return render(request,'servicecenter/confirmcar.html',context)

def pickedup(request):
	cars = CarServiceRequest.objects.filter(servicestatus = 'PICKED UP')
	context = {'cars':cars}

	return render(request,'servicecenter/pickedup.html',context)

def servicestarted(request):
	cars = CarServiceRequest.objects.filter(servicestatus = 'SERVICE STARTED')
	context = {'cars':cars}

	return render(request,'servicecenter/servicestarted.html',context)

def servicecomplete(request):
	cars = CarServiceRequest.objects.filter(servicestatus = 'SERVICE COMPLETED')
	context = {'cars':cars}

	return render(request,'servicecenter/servicecomplete.html',context)

def outfordelivery(request):
	cars = CarServiceRequest.objects.filter(servicestatus = 'OUT FOR DELIVERY')
	context = {'cars':cars}

	return render(request,'servicecenter/outfordelivery.html',context)

def payment(request):
	cars = CarServiceRequest.objects.filter(servicestatus = 'PAYMENT DONE')
	context = {'cars':cars}

	return render(request,'servicecenter/payment.html',context)

def delivered(request):
	cars = CarServiceRequest.objects.filter(servicestatus = 'DELIVERED')
	context = {'cars':cars}

	return render(request,'servicecenter/delivered.html',context)

