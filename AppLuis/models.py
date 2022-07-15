from mailbox import NoSuchMailboxError
from django.db import models
# Create your models here.
class Familia(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    tlf=models.IntegerField()
    FechNac=models.DateField()

class Carrera(models.Model):
    profesion=models.CharField(max_length=50)
    Universidad=models.CharField(max_length=50)
    email= models.EmailField()

class Mascotas(models.Model):
    nombre=models.CharField(max_length=50)
    Tipo=models.CharField(max_length=50)
    Raza=models.CharField(max_length=50)
    
