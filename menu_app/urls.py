from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu, name='menu'),
    path('module/<str:module_name>/', views.module, name='module'),
    path('alumnos/', views.alumnos_list, name='alumnos_list'),
    path('alumnos/create/', views.alumno_create, name='alumno_create'),
]
