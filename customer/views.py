from django.shortcuts import render,redirect
from django.http import HttpResponse

from servicecenter.forms import CarServiceForm, BikeServiceForm
from .forms import RegistrationForm,CarRegistration,BikeRegistration
from .forms import LoginForm
from .models import Register,CarVehicle,BikeVehicle
from servicecenter.models import CarServiceCenter, BikeServiceCenter, CarServiceRequest, BikeServiceRequest
from administrator.models import CarManufacturer,BikeManufacturer
# Create your views here.


def index(request):
	carcenter=CarServiceCenter.objects.all()
	bikecenter=BikeServiceCenter.objects.all()
	context={'carcenter':carcenter,'bikecenter':bikecenter}
	return render(request,'customer/index.html',context)

def dashboard(request):
	try:
		if request.session['username'] is None:
			return redirect('/customer/login')
	except:
		return redirect('/customer/login')

	registers=Register.objects.filter(email=request.session['username'])
	cars=CarVehicle.objects.filter()
	bikes=BikeVehicle.objects.filter()
	carcenter=CarServiceCenter.objects.filter()
	bikecenter=BikeServiceCenter.objects.filter()
	context={'registers':registers,'cars':cars,'bikes':bikes,'carcenter':carcenter,'bikecenter':bikecenter}
	return render(request,'customer/dashboard.html',context)

           
def register(request):
	form=RegistrationForm(request.POST or None)
	if request.method=="POST":
		if form.is_valid():
			try:
				form.save()
				return redirect('/customer/login')
			except:
				return redirect('/customer/register')
	context={'form':form}
	return render(request,'customer/register.html',context)

def login(request):
	form=LoginForm(request.POST or None)
	if request.method=="POST":
		if form.is_valid():
			username=form.cleaned_data.get('username')
			password=form.cleaned_data.get('password')
			try:
				user=Register.objects.get(email=username,password=password)
				request.session['username']=user.email
				return redirect('/customer/dashboard')
			except:
				return HttpResponse("<p> Sorry, Login failed</p>")

	context={'form':form}
	return render(request,'customer/login.html',context)

def car_register(request):
	try:
		if request.session['username'] is None:
			return redirect('/customer/login')
	except:
		return redirect('/customer/login')
	form=CarRegistration(request.POST or None, initial ={'owned_by': request.session['username']})
	if request.method=="POST":
		if form.is_valid():
			try:
				form.save()
				return redirect('/customer/dashboard')
			except:
				 return redirect('/customer/car_register')
	context={'form':form}
	return render(request,'customer/customer_car_register.html',context)

def bike_register(request):
	try:
		if request.session['username'] is None:
			return redirect('/customer/login')
	except:
		return redirect('/customer/login')

	form=BikeRegistration(request.POST or None, initial ={'owned_by': request.session['username'],'vehicle_type':'BIKE'})
	if request.method=="POST":
		if form.is_valid():
			try:
				form.save()
				return redirect('/customer/dashboard')
			except:
			 return redirect('/customer/bike_register')
	context={'form':form}
	return render(request,'customer/customer_bike_register.html',context)

def logout(request):
	for key in list(request.session.keys()):
		del request.session[key]
	return redirect('/customer')

def carservice_detail(request,id):
	carcenterid=CarServiceCenter.objects.get(id=id)
	context={'carcenterid':carcenterid}
	return render(request,'customer/carservice_detail.html',context)

def bikeservice_detail(request,id):
	bikecenterid=BikeServiceCenter.objects.get(id=id)
	context={'bikecenterid':bikecenterid}
	return render(request,'customer/bikeservice_detail.html',context)

def rent(request):
	return render(request,'customer/rent.html')

def carservicerequest(request,vehicle_no):
	try:
		if request.session['username'] is None:
			return redirect('/customer/login')
	except:
		return redirect('/customer/login')
	carno = CarVehicle.objects.get(vehicle_no = vehicle_no).vehicle_no

	form=  CarServiceForm(request.POST or None, initial={'vehicle_no':carno,'owned_by':request.session['username']})
	if request.method=='POST':
		if form.is_valid():
			try :
				form.save()
				return redirect('/customer/carbookingstatus')
			except:
				HttpResponse("<h3> unable to process your request now </h3>")

	context={'form':form}
	return render(request,'customer/carservicerequest.html',context)

def bikeservicerequest(request,vehicle_no):
	try:
		if request.session['username'] is None:
			return redirect('/customer/login')
	except:
		return redirect('/customer/login')
	bikeno = BikeVehicle.objects.get(vehicle_no = vehicle_no).vehicle_no

	form=  BikeServiceForm(request.POST or None, initial={'vehicle_no':bikeno,'owned_by':request.session['username']})
	if request.method=='POST':
		if form.is_valid():
			try :
				form.save()
				return redirect('/customer/bikebookingstatus')
			except:
				HttpResponse("<h3> unable to process your request now </h3>")



	context={'form':form}
	return render(request,'customer/bikeservicerequest.html',context)

def carlist(request):
	cars = CarVehicle.objects.filter(owned_by = request.session['username'])
	context ={'cars':cars}
	return  render(request,'customer/carlist.html',context)

def bikelist(request):
	bikes = BikeVehicle.objects.filter(owned_by = request.session['username'])
	context ={'bikes':bikes}
	return  render(request,'customer/bikelist.html',context)


def carbookingstatus(request):
	cars = CarServiceRequest.objects.filter(owned_by = request.session['username'])
	context ={'cars':cars}
	return  render(request,'customer/carbookingstatus.html',context)

def bikebookingstatus(request):
	bikes = BikeServiceRequest.objects.filter(owned_by = request.session['username'])
	context ={'bikes':bikes}
	return  render(request,'customer/bikebookingstatus.html',context)

def cancelbyownercar(request,id):
	booking = CarServiceRequest.objects.get(id = id)
	if booking.servicestatus =='REQUEST BOOKING':
		booking.servicestatus = 'CANCELLED BY OWNER'
		booking.save()
		return HttpResponse("<h3> Your booking is cancelled</h3>")
	elif booking.servicestatus == 'CANCELLED BY OWNER':
		return HttpResponse("<h3> Your booking is already cancelled by You</h3>")
	elif booking.servicestatus == 'CANCELLED BY ADMIN ON OWNERS REQUEST':
		return HttpResponse("<h3> Your booking is already cancelled by Admin on your request</h3>")
	else:
		return HttpResponse("<h3> You cannot cancel this booking, Request Service Center for Cancellation of Booking</h3>")

def changestatuscar(request,id,status):
	booking = CarServiceRequest.objects.get(id = id)
	booking.servicestatus = status
	booking.save()
	return  HttpResponse ("<h3> Booking status is changed to ",status,"</h3>")


def changestatusbike(request,id,status):
	booking = BikeServiceRequest.objects.get(id = id)
	booking.servicestatus = status
	booking.save()
	return  HttpResponse ("<h3> Booking status is changed to ",status,"</h3>")

