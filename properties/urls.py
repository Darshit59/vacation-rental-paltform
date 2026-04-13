from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name="home"),

    path('property/<int:id>/', views.property_detail, name="property_detail"),

    path('host-dashboard/', views.host_dashboard, name="host_dashboard"),

    path('add-property/', views.add_property, name="add_property"),

    path('edit-property/<int:id>/', views.edit_property, name="edit_property"),

    path('delete-property/<int:id>/', views.delete_property, name="delete_property"),

    path('upload-image/<int:id>/', views.upload_image, name="upload_image"),
    
    path('properties/', views.property_list, name="property_list"),
    
    path('booking/<int:id>/', views.booking_page, name="booking_page"),
    
    path('register/', views.register, name='register'),

    path('verify-otp/', views.verify_otp, name='verify_otp'),


]