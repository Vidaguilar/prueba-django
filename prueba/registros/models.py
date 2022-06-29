from django.db import models
class Alumnos(models.Model): #Define la estructura de nuestra tabla
    matricula = models.CharField(max_length=12,verbose_name="Mat") #Texto corto
    nombre = models.TextField() #Texto largo
    carrera = models.TextField()
    turno = models.CharField(max_length=10)
    imagen = models.ImageField(null=True,upload_to="fotos",verbose_name="Fotografía")
    created = models.DateTimeField(auto_now_add=True) #Fecha y tiempo
    updated = models.DateTimeField(auto_now_add=True)
    class Meta:
         verbose_name = "Alumno"
         verbose_name_plural = "Alumnos"
         ordering = ["-created"] 
    def __str__(self):
         return self.nombre

# Create your models here.
