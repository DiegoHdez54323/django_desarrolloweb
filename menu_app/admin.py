from django.contrib import admin
from .models import Alumno

@admin.register(Alumno)
class AlumnoADmin(admin.ModelAdmin):
    list_display = ("matricula","nombre","apellido","email","fecha_nacimiento","fecha_registro")
    search_fields = ("matricula","nombre","apellido","email")
