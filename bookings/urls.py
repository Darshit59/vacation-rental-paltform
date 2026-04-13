from django.urls import path
from . import views

urlpatterns = [

    path('host-bookings/', views.host_bookings, name='host_bookings'),

    path('approve-booking/<int:id>/', views.approve_booking, name='approve_booking'),

    path('reject-booking/<int:id>/', views.reject_booking, name='reject_booking'),

   path('booking-success/<int:booking_id>/',views.booking_success,name='booking_success'),
   
    path('booking/pdf/<int:booking_id>/',views.download_booking_pdf,name='booking_pdf'),
]