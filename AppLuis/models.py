
from django.db import models
# Create your models here.
class Familia(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    tlf=models.IntegerField()
    FechNac=models.DateField()
    
    def __str__(self):
        return self.nombre+" "+str(self.apellido)+" "+str(self.tlf)+" "+str(self.FechNac)


class Carrera(models.Model):
    profesion=models.CharField(max_length=50)
    Universidad=models.CharField(max_length=50)
    email= models.EmailField()
    
    def __str__(self):
        return self.profesion+" "+str(self.Universidad)+" "+str(self.email)

class Mascotas(models.Model):
    nombre=models.CharField(max_length=50)
    Tipo=models.CharField(max_length=50)
    Raza=models.CharField(max_length=50)
   
    def __str__(self):
        return self.nombre+" "+str(self.Tipo)+" "+str(self.Raza)
