from django.urls import path
from . import views

urlpatterns = [ 
    path('',views.administrar_estudiantes, name="AdministrarEstudiantes"), 
    path('cambiarestatus/<int:estudiante_id>/', views.cambiar_estatus, name='CambiarEstatus'),
    path('editarestudiante/<str:id>/', views.editar_estudiantes, name='EditarEstudiante'),
    path('estudiantes/<str:id>/', views.estudiante_editado, name='EstudianteEditado'),
]
