from menu_app.models import Alumno
from django.shortcuts import render

def menu(request):
    return render(request, 'menu.html')