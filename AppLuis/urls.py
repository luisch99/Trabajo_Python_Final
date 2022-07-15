from django.urls import path
from .views import *


urlpatterns = [
    path('Familia/', Familia, name='Familia'),
    path('Carrera/', Carrera, name='Carrera'),
    path('Mascotas/', Mascotas, name='Mascotas'),
    path('', inicio, name='Inicio'),
]