from django.contrib import admin
from django.urls import path, include
from properties import views   # ✅ correct import

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path('admin/', admin.site.urls),

    # HOME PAGE
    path('', views.home, name='home'),

    # Properties app
    path('', include('properties.urls')),

    # Users app
    path('', include('users.urls')),

    # Bookings app
    path('', include('bookings.urls')),
    
    path('', include('messaging.urls')),

   
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)