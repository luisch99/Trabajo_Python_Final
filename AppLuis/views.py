from email.errors import NoBoundaryInMultipartDefect
from django.http import HttpResponse
from django.shortcuts import render
from AppLuis.models import Familia
# Create your views here.

def Fami(self):

    familia1=Familia(nombre="Raquel Andrea",apellido="Chuquichanca Cañari",tlf=988127372,FechNac="1997-06-10")
    familia2=Familia(nombre="Luis Adrian",apellido="Chuquichanca Cañari",tlf=984823123,FechNac="1999-08-05")
    familia3=Familia(nombre="Godofredo",apellido="Chuquichanca San Miguel",tlf=983823211,FechNac="1962-09-11")
    familia4=Familia(nombre="Edith Doris",apellido="Cañari Bazam",tlf=983823211,FechNac="1960-07-11")
    
    texto=f"Familiar creado: {familia1.nombre} {familia1.apellido} {familia1.tlf} {familia1.FechNac}"
    texto2=f"Familiar creado: {familia2.nombre} {familia2.apellido} {familia2.tlf} {familia2.FechNac}"
    texto3=f"Familiar creado: {familia3.nombre} {familia3.apellido} {familia3.tlf} {familia3.FechNac}"
    texto4=f"Familiar creado: {familia4.nombre} {familia4.apellido} {familia4.tlf} {familia4.FechNac}"

    return HttpResponse(texto+"<br>"+texto2+"<br>"+texto3+"<br>"+texto4)

