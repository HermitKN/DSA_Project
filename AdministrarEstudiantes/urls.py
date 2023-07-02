from django.urls import path
from . import views

urlpatterns = [ 
    path('',views.administrar_estudiantes, name="AdministrarEstudiantes"), 
    path('cambiarestatus/<int:estudiante_id>/', views.cambiar_estatus, name='CambiarEstatus'),
]
