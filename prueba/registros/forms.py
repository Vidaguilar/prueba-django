from django import forms
from .models import ComentarioContacto
from.models import Alumnos
class ComentarioContactoForm(forms.ModelForm):
 class Meta:
    model = ComentarioContacto
    fields = ['usuario','mensaje']
class AlumnosForm(forms.ModelForm):
 class Meta:
    model = Alumnos
    fields = ['turno','carrera','nombre']