from django.urls import path
from .views import alumno_create, alumnos_list, menu, module

urlpatterns = [
    path('', menu, name='menu'),
    path('module/<str:module_name>/', module, name='module'),
    path('alumnos/', alumnos_list, name='alumnos_list'),
    path('alumnos/create/', alumno_create, name='alumno_create'),
]
