from django.urls import path
from .views import *


urlpatterns = [
    path('', inicio, name='Inicio'),
    path('Familia/', Familia, name='Familia'),
    path('Carrera/', Carrera, name='Carrera'),
    path('Mascotas/', Mascotas, name='Mascotas'),
    path('Formulario/', Formulario, name='Formulario'),
    path('carreraFormulario/', carreraFormulario, name='carreraFormulario'),
    path('busquedaNombre/', busquedaNombre, name='busquedaNombre'),
    path('buscar/', buscar, name='buscar'),
]