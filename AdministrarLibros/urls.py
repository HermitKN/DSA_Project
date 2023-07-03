from django.urls import path
from . import views

urlpatterns = [ 

    path('',views.administrar_libros, name="AdministrarLibros"),
    path('eliminarlibro/<str:id>/', views.eliminar_libro, name='Eliminarlibro')
]