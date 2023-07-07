from django.urls import path
from .import views

urlpatterns = [ 

    path('',views.notas_prestamo, name="NotasPrestamo"),
    #path('cambiarpenalizacion/<int:prestamo_id>/', views.cambiar_penalizacion, name='CambiarPenalizacion'),
    #path('editarcantidaddevuelta/<int:prestamo_id>/', views.editar_cantidad_devuelta, name='EditarCantidadDevuelta'),
]