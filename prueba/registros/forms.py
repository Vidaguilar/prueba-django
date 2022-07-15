from django import forms
from .models import ComentarioContacto
from.models import Alumnos
from .models import Archivos
from django.forms import ModelForm, ClearableFileInput
class ComentarioContactoForm(forms.ModelForm):
 class Meta:
    model = ComentarioContacto
    fields = ['usuario','mensaje']
class AlumnosForm(forms.ModelForm):
 class Meta:
    model = Alumnos
    fields = ['turno','carrera','nombre']

class CustomCleareableFileInput(ClearableFileInput):
   template_whit_clear='<br><label for="%(clear_checbox_id)s">%(clear_checbox_label)s</label>%(clear)s'

class FormArchivo(ModelForm):
   class Meta:
    model = Archivos
    fields = ['titulo','descripcion','archivo']
    widgets ={
      'archivo':CustomCleareableFileInput
    }