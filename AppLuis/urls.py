from django.urls import path
from .views import *


urlpatterns = [
    path('Familia/', Familia),
    path('Carrera/', Carrera),
    path('Mascotas/', Mascotas),
    path('', inicio),
]