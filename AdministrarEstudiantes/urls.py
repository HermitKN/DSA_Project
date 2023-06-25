from django.urls import path
from . import views

urlpatterns = [ 
    # se importa la ruta de la url de la app que viene desde la url de Biblioteca con include
    path('',views.administrar_estudiantes, name="AdministrarEstudiantes"), 
]
