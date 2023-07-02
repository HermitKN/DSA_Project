from django.urls import path
from .import views

urlpatterns = [ 

    path('',views.notas_prestamo, name="NotasPrestamo"),
    path('cambiarpenalizacion/<int:prestamo_id>/', views.cambiar_penalizacion, name='CambiarPenalizacion'),
]