from django.urls import path
from .import views

urlpatterns=[
            path('servicecenters_home/',views.servicecenters_home),
            path('car_servicecenter_register_form/',views.car_servicecenter_register_form),
            path('bike_servicecenter_register_form/',views.bike_servicecenter_register_form),
            path('car_service_center_login',views.car_service_center_login),
            path('bike_service_center_login',views.bike_service_center_login),
            path('dashboard',views.dashboard),
            path('newbooking', views.newbooking),
            path('newbookingbike', views.newbookingbike),
            path('costestimation/<id>',views.costestimation),
            path('changestatuscar/<id>/<servicestatus>',views.changestatuscar),
            path('confirmcar',views.confirmcar),
            path('pickedup',views.pickedup),
            path('servicestarted',views.servicestarted),

            path('servicecomplete',views.servicecomplete),

            path('payment',views.payment),

            path('outfordelivery',views.outfordelivery),

            path('delivered',views.delivered),



         
]
