from django.urls import path
from . import views

urlpatterns = [ 

    path('',views.administrar_libros, name="Libros"),
]