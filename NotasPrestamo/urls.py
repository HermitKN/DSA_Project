from django.urls import path
from NotasPrestamo import views

urlpatterns = [ 

    path('notas',views.notas_prestamo, name="NotasPrestamo"),
]