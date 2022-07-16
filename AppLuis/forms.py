from django import forms


class FamiliaForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido= forms.CharField(max_length=50)
    tlf=forms.IntegerField()
    FechNac=forms.DateField()

class CarreraForm(forms.Form):
    profesion = forms.CharField(max_length=50)
    Universidad = forms.CharField(max_length=50)
    email =forms.EmailField()
