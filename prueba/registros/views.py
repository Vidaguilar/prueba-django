from django.shortcuts import render
from .models import Alumnos, Comentario, ComentarioContacto 
from .forms import ComentarioContactoForm
from .forms import AlumnosForm
from django.shortcuts import get_object_or_404
import datetime

# Create your views here.
def registros(request):
 alumnos=Alumnos.objects.all()
 return render(request,"registros/principal.html",{'alumnos':alumnos})

def consulta1(request):
 alumnos=Alumnos.objects.filter(carrera="TI")
 return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consulta2(request):
 alumnos=Alumnos.objects.filter(carrera="TI").filter(turno="Matutino")
 return render(request,"registros/consultas.html",{'alumnos':alumnos})
def consulta3(request):
 alumnos=Alumnos.objects.all().only("matricula","nombre","carrera","turno","imagen")
 return render(request,"registros/consultas.html",{'alumnos':alumnos})
def consulta4(request):
 alumnos=Alumnos.objects.filter(turno__contains='Vesp')
 return render(request,"registros/consultas.html",{'alumnos':alumnos})
def consulta5(request):
 alumnos=Alumnos.objects.filter(nombre__in=["Juan","Ana"])
 return render(request,"registros/consultas.html",{'alumnos':alumnos})
def consulta6(request):
 fechai=datetime.date(2022,7,1)
 fecha=datetime.date(2022,7,15)
 alumnos=Alumnos.objects.filter(created__range=(fechai,fecha))
 return render(request,"registros/consultas.html",{'alumnos':alumnos})
def consulta7(request):
 alumnos=Alumnos.objects.filter(comentario__coment__contains="es un")
 return render(request,"registros/consultas.html",{'alumnos':alumnos})
def eliminaralumno(request,matricula,confimacion='registros/conel2.html'):
    alumno = get_object_or_404(Alumnos, matricula=matricula)
    if request.method=='POST':
        alumno.delete()
        alumnos=Alumnos.objects.all()
        return render(request,"registros/principal.html",{'alumnos':alumnos})
    return render (request, confimacion,{'object':alumno})

def editaral(request,matricula,):
    alumno = get_object_or_404(Alumnos,matricula=matricula)
    return render(request,"registros/edital.html",{'alumno':alumno})

def editaralum(request,matricula,):
    alumno = get_object_or_404(Alumnos,matricula=matricula)
    form= AlumnosForm(request.POST,instance=alumno)
    if form.is_valid():
        form.save()
        alumnos=Alumnos.objects.all()
        return render(request,"registros/principal.html",{'alumnos':alumnos})
    return render(request,"registros/edital.html",{'alumno':alumno})

def registrar(request):
    if request.method == 'POST':
     form = ComentarioContactoForm(request.POST)
    if form.is_valid(): #Si los datos recibidos son correctos
        form.save() #inserta
        comentarioContacto=ComentarioContacto.objects.all()
        return render(request ,"registros/vercoment.html",{'comentariocontactos':comentarioContacto})
    form = ComentarioContactoForm()
    #Si algo sale mal se reenvian al formulario los datos ingresados
    return render(request,'registros/contacto.html',{'form': form}) 

def contacto(request):
 return render(request,"registros/contacto.html")

def coments(request):
 comentarioContacto=ComentarioContacto.objects.all()
 return render(request,"registros/vercoment.html",{'comentariocontactos':comentarioContacto})

def eliminarComentarioContacto(request,id,confimacion='registros/conel.html'):
    comentario = get_object_or_404(ComentarioContacto, id=id)
    if request.method=='POST':
        comentario.delete()
        comentarioContacto=ComentarioContacto.objects.all()
        return render(request,"registros/vercoment.html",{'comentariocontactos':comentarioContacto})
    return render (request, confimacion,{'object':comentario})

def editar(request,id,):
    comentario = get_object_or_404(ComentarioContacto,id=id)
    return render(request,"registros/edit.html",{'comentario':comentario})

def editarcom(request,id,):
    comentario = get_object_or_404(ComentarioContacto,id=id)
    form= ComentarioContactoForm(request.POST,instance=comentario)
    if form.is_valid():
        form.save()
        comentarios=ComentarioContacto.objects.all()
        return render(request,"registros/vercoment.html",{'comentariocontactos':comentarios})
    return render(request,"registros/edit.html",{'comentario':comentario})
    

