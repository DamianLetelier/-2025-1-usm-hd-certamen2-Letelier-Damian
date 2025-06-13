from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('comunas/', include('MisComunas.urls')),  # Asegúrate de cambiar "tuapp" por el nombre real de tu app
    path('', lambda request: redirect('comuna_list')),  # Redirige la raíz al listado de comunas
]
