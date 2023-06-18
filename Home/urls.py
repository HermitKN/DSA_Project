from django.urls import path
from Home import views

urlpatterns = [ 

    path('',views.home, name="Home"),
    path('notas',views.notas_prestamo, name="NotasPrestamo"),
    path('libros',views.administrar_libros, name="Libros"),
    path('libros',views.administrar_estudiantes, name="Estudiantes"),
]
