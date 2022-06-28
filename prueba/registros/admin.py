from django.contrib import admin
from .models import Alumnos
# Register your models here.
class AdministrarModelo(admin.ModelAdmin):
 readonly_fields = ('created', 'updated'
)
admin.site.register(Alumnos,AdministrarModelo)

# Register your models here.
