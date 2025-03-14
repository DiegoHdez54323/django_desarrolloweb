from menu_app.models import Alumno

from django.shortcuts import render

def alumnos_list(request):
    # Se obtiene la lista de alumnos
    alumnos = Alumno.objects.all().order_by('nombre')
    
    # Se renderiza la plantilla 'alumnos_list.html' pasando la lista de alumnos
    return render(request, 'alumnos_list.html', {
        'alumnos': alumnos
    })