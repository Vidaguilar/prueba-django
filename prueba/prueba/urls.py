"""prueba URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from inicio import views
from django.conf import settings
from registros import views as views_registros
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views_registros.registros, name="Principal"),
    path('',views.principal, name="principal"),
    path('cont/',views_registros.contacto, name="contacto"),
    path('formulario/',views.formulario, name="formulario"),
     path('ejem/',views.ejemplo, name="ejemplo"),
    path('registrar/',views_registros.registrar,name="Registrar"),
    path('ver/',views_registros.coments, name="coments"),
    path("condel/<int:id>/",views_registros.eliminarComentarioContacto, name="Eliminar"),
    path("edit/<int:id>/",views_registros.editar, name="Editar"),
    path("editar/<int:id>/",views_registros.editarcom, name="Editarcom"),
    path("condel2/<matricula>/",views_registros.eliminaralumno, name="Eliminaral"),
    path("edital/<matricula>/",views_registros.editaral, name="Editaral"),
    path("editaralum/<matricula>/",views_registros.editaralum, name="Editaralu"),
    path("con1/",views_registros.consulta1,name="Consultas"),
    path("con2/",views_registros.consulta2,name="Consultas2"),
    path("con3/",views_registros.consulta3,name="Consultas3"),
    path("con4/",views_registros.consulta4,name="Consultas4"),
    path("con5/",views_registros.consulta5,name="Consultas5"),
    path("con6/",views_registros.consulta6,name="Consultas6"),
    path("con7/",views_registros.consulta7,name="Consultas7"),
    path('subir',views_registros.archivos,name="Subir"),
     path("consultasQL/",views_registros.consultasSQL,name="sql"),
]
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)