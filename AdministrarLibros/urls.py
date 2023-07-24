from django.urls import path
from . import views

urlpatterns = [ 

    path('',views.administrar_libros, name="AdministrarLibros"),
    path('eliminarlibro/<str:id>/', views.eliminar_libro, name='Eliminarlibro'),
    path('editarlibro/<str:id>/', views.editar_libros, name='Editarlibro'),
    path('libros/<str:id>/', views.libro_editado, name='LibroEditado'),
    path('verlibros/', views.dataTable, name='VisualizarLibros'),
    path('buscar/', views.buscarid, name='BuscarID')
]