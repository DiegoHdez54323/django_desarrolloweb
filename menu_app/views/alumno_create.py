from menu_app.models import Alumno

from django.http import JsonResponse

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