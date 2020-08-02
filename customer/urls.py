from django.urls import path
from.import views
urlpatterns =[
		path('',views.index),
		path('register/',views.register),
		path('login/',views.login),
		path('logout/',views.logout),
		path('car_register/',views.car_register),
		path('bike_register/',views.bike_register),
		path('dashboard/',views.dashboard),
		path('carlist', views.carlist),
		path('bikelist', views.bikelist),
		path('carbookingstatus', views.carbookingstatus),
		path('bikebookingstatus', views.bikebookingstatus),
        path('carservicerequest/<vehicle_no>',views.carservicerequest),
		path('bikeservicerequest/<vehicle_no>',views.bikeservicerequest),
		path('carservice_detail/<id>',views.carservice_detail),
        path('bikeservice_detail/<id>',views.bikeservice_detail),
        path('rent/',views.rent),
		path('cancelbyownercar/<id>',views.cancelbyownercar)
]