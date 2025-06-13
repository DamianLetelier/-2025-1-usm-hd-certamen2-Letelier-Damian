from django.urls import path
from . import views

urlpatterns = [
    path('', views.comuna_list, name='comuna_list'),
    path('nueva/', views.comuna_create, name='comuna_create'),
    path('editar/<int:pk>/', views.comuna_update, name='comuna_update'),
    path('eliminar/<int:pk>/', views.comuna_delete, name='comuna_delete'),
]
