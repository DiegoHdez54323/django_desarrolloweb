from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from .models import Alumno

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets
from .serializers import AlumnoSerializer

class AlumnoViewSet(View):
    def get(self, request, id = 0):
        if (id > 0):
            MisAlumnos = list(Alumno.objects.values())
            if (len(MisAlumnos) > 0):
                alumno = MisAlumnos[0]
                msm = {'message': 'Exito', 'Alumno': alumno}
            else:
                msm = {'message': 'No hay alumnos registrados'}
            return JsonResponse(msm)
        else:
            MisAlumnos = list(Alumno.objects.values())
            if (len(MisAlumnos) > 0):
                msm = {'message': 'Exito', 'Alumno': MisAlumnos}
            else:
                msm = {'message': 'No hay alumnos registrados'}
            return JsonResponse(msm)
    



def menu(request):
    return render(request, 'menu.html')

def module(request, module_name):
    message = f"Bienvenido al módulo de {module_name}."
    
    # Se renderiza la plantilla 'module.html' pasando el nombre del módulo y el mensaje
    return render(request, 'module.html', {
        'module_name': module_name,
        'message': message
    })

def alumnos_list(request):
    # Se obtiene la lista de alumnos
    alumnos = Alumno.objects.all().order_by('nombre')
    
    # Se renderiza la plantilla 'alumnos_list.html' pasando la lista de alumnos
    return render(request, 'alumnos_list.html', {
        'alumnos': alumnos
    })

def alumno_create(request):
    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        matricula = request.POST.get('matricula')
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        email = request.POST.get('email')
        fecha_nacimiento = request.POST.get('fecha_nacimiento')
        try:
            alumno = Alumno.objects.create(
                matricula=matricula,
                nombre=nombre,
                apellido=apellido,
                email=email,
                fecha_nacimiento=fecha_nacimiento
            )
            data = {
                'matricula': alumno.matricula,
                'nombre': alumno.nombre,
                'apellido': alumno.apellido,
                'email': alumno.email,
                'fecha_nacimiento': alumno.fecha_nacimiento.strftime('%d/%m/%Y') if hasattr(alumno.fecha_nacimiento, 'strftime') else alumno.fecha_nacimiento,
                'fecha_registro': alumno.fecha_registro.strftime('%d/%m/%Y %H:%M') if hasattr(alumno.fecha_registro, 'strftime') else alumno.fecha_registro,
            }
            return JsonResponse({'success': True, 'alumno': data})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    return JsonResponse({'success': False, 'error': 'Invalid request method.'})

