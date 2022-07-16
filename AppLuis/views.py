
from ast import Return
from urllib import request
from django.http import HttpResponse
from django.shortcuts import render, HttpResponse
from AppLuis.models import Carrera, Familia, Mascotas
from AppLuis.forms import FamiliaForm, CarreraForm

# Create your views here.

def Fami(self):

    familia1=Familia(nombre="Raquel Andrea",apellido="Chuquichanca Cañari",tlf=988127372,FechNac="1997-06-10")
    familia2=Familia(nombre="Luis Adrian",apellido="Chuquichanca Cañari",tlf=984823123,FechNac="1999-08-05")
    familia3=Familia(nombre="Godofredo",apellido="Chuquichanca San Miguel",tlf=983823211,FechNac="1962-09-11")
    familia4=Familia(nombre="Edith Doris",apellido="Cañari Bazan",tlf=983823211,FechNac="1960-07-11")
    
    texto=f"Familiar creado: {familia1.nombre} {familia1.apellido} {familia1.tlf} {familia1.FechNac}"
    texto2=f"Familiar creado: {familia2.nombre} {familia2.apellido} {familia2.tlf} {familia2.FechNac}"
    texto3=f"Familiar creado: {familia3.nombre} {familia3.apellido} {familia3.tlf} {familia3.FechNac}"
    texto4=f"Familiar creado: {familia4.nombre} {familia4.apellido} {familia4.tlf} {familia4.FechNac}"

    return HttpResponse(texto+"<br>"+texto2+"<br>"+texto3+"<br>"+texto4)

def Carre(self):

    carrera1=Carrera(profesion="Derecho Corporativo",Universidad="Esan")
    carrera2=Carrera(profesion="Ingenieria de Sistemas",Universidad="Esan")
    carrera3=Carrera(profesion="Ingenieria Industrial",Universidad="Uni")
    carrera4=Carrera(profesion="Enfermera",Universidad="San Marcos")
    carrera1.save()
    carrera2.save()
    carrera3.save()
    carrera4.save()
    texto=f"Carrera creado: {carrera1.profesion} {carrera1.Universidad} "
    texto2=f"Carrera creado: {carrera2.profesion} {carrera2.Universidad} "
    texto3=f"Carrera creado: {carrera3.profesion} {carrera3.Universidad} "
    texto4=f"Carrera creado: {carrera4.profesion} {carrera4.Universidad} "

    return HttpResponse(texto+"<br>"+texto2+"<br>"+texto3+"<br>"+texto4)

def Masco(self):

    Mascota1=Mascotas(nombre="Pelusa",Tipo="Gato",Raza="Siames")
    Mascota2=Mascotas(nombre="Bobby",Tipo="Perro",Raza="Labrador")
    Mascota3=Mascotas(nombre="Nico",Tipo="Perro",Raza="Golden Retriever")
    Mascota4=Mascotas(nombre="Golden",Tipo="Pez",Raza="Pez Dorado")
    Mascota1.save()
    Mascota2.save()
    Mascota3.save()
    Mascota4.save()
    texto=f"Mascota creado: {Mascota1.nombre} {Mascota1.Tipo} {Mascota1.Raza}"
    texto2=f"Mascota creado: {Mascota2.nombre} {Mascota2.Tipo} {Mascota2.Raza}"
    texto3=f"Mascota creado: {Mascota3.nombre} {Mascota3.Tipo} {Mascota3.Raza}"
    texto4=f"Mascota creado: {Mascota4.nombre} {Mascota4.Tipo} {Mascota4.Raza}"

    return HttpResponse(texto+"<br>"+texto2+"<br>"+texto3+"<br>"+texto4)

def inicio(request):
    return render(request, "AppLuis/inicio.html")

def Familia(request):
    return render(request, "AppLuis/Familia.html")

def Carrera(request):
    return render(request, "AppLuis/Carrera.html")

def Mascotas(request):
    return render(request, "AppLuis/Mascotas.html")

def Formulario(request):

    if (request.method=="POST"):
        form=FamiliaForm(request.POST)
        print(form)
        if form.is_valid():
            info=form.cleaned_data
            print(info)
            nombre=info["nombre"]
            apellido=info["apellido"]
            tlf=info["tlf"]
            FechNac=info["FechNac"]
            familia= Familia(nombre=nombre, apellido=apellido, tlf=tlf, FechNac=FechNac)
            familia.save()
            return render (request, "AppLuis/inicio.html")
    else:
        form=FamiliaForm()
    return render(request, "AppLuis/Formulario.html", {"formulario":form})


def carreraFormulario(request):

    if request.method=="POST":
        form= CarreraForm(request.POST)
        if form.is_valid():
            info= form.cleaned_data
            profesion= info["profesion"]
            Universidad= info["Universidad"]
            email= info["email"]
            carrera= Carrera(profesion=profesion, Universidad=Universidad, email=email)
            carrera.save()
            return render (request, "AppLuis/inicio.html")
    else:
        form=CarreraForm()
    return render(request, "AppLuis/carreraForm.html", {"formulario":form})
    

def busquedaNombre(request):
    return render(request, "AppLuis/busquedaNombre.html")

def buscar(request):
    if request.GET["nombre"]:
        nomb= request.GET["nombre"]
        familias=Familia.objects.filter(nombre=nomb)
        return render(request, "AppLuis/resultadosBuqueda.html", {"familias":familias})
    else:
        return render(request, "AppLuis/busquedaNombre.html", {"error": "No se ingreso ningun nombre"})
    