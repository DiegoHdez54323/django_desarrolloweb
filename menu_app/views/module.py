from menu_app.models import Alumno

from django.shortcuts import render

def module(request, module_name):
    """
    Vista para cada módulo.
    
    Si se selecciona "Salir", se muestra un mensaje especial.
    Para las demás opciones, se muestra un mensaje de bienvenida indicando el módulo.
    """
    
    message = f"Bienvenido al módulo de {module_name}."
    
    # Se renderiza la plantilla 'module.html' pasando el nombre del módulo y el mensaje
    return render(request, 'module.html', {
        'module_name': module_name,
        'message': message
    })