from django.urls import path
from . import views

urlpatterns = [ 

    path('',views.notas_prestamo, name="Notas"),
]