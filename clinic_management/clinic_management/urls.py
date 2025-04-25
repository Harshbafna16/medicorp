from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('clinic.urls')),  # Ensure clinic app URLs are included
]
