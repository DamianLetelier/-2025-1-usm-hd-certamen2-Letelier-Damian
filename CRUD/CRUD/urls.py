from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('comunas/', include('MisComunas.urls')), 
    path('', lambda request: redirect('comuna_list')),  
]
