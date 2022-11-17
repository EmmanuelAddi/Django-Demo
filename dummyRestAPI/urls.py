from django.contrib import admin
from django.conf.urls import include
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mainApp/', include('mainApp.urls')),
    path('viewsets/', include('viewsets.urls')),
]
