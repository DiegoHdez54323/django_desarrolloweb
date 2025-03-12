from django.urls import path, include
from . import views
from .views import AlumnoViewSet

from rest_framework.routers import DefaultRouter
from rest_framework import routers

#router = DefaultRouter()

#router = routers.DefaultRouter()
#router.register(r'alumnos', views.AlumnoViewSet)

urlpatterns = [
    path('', views.menu, name='menu'),
    path('module/<str:module_name>/', views.module, name='module'),
    #path('alumnos/', views.alumnos_list, name='alumnos_list'),
    path('alumnos/create/', views.alumno_create, name='alumno_create'),
    
    ### API URLS
    path('alumnos/', AlumnoViewSet.as_view(), name='alumnos'),
    path('alumnos/<int:id>/', AlumnoViewSet.as_view(), name='alumnos_detalle'),
    #path('api/', include(router.urls)),
]
