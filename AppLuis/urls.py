from django.urls import path
from .views import *


urlpatterns = [
    path('', inicio, name='Inicio'),
    path('Familia/', Familias, name='Familia'),
    path('Carrera/', Carreras, name='Carrera'),
    path('Mascotas/', Mascotass, name='Mascotas'),
    path('Formulario/', Formulario, name='Formulario'),
    path('carreraFormulario/', carreraFormulario, name='carreraFormulario'),
    path('mascotasFormulario/', mascotasFormulario, name='mascotasFormulario'),
    path('busquedaNombre/', busquedaNombre, name='busquedaNombre'),
    path('buscar/', buscar, name='buscar'),
]