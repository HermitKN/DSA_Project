from django.db import models
from AdministrarLibros.models import Libro
from AdministrarEstudiantes.models import Estudiante
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from datetime import datetime, timedelta
from django.core.validators import MinValueValidator

# Create your models here.

TIPO_CHOICES = (
    ('Interno', 'Interno'),
    ('Externo', 'Externo'),
)

class Prestamo(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="Nota de Prestamo")
    estudiante=models.ForeignKey(Estudiante, on_delete=models.CASCADE, verbose_name="Estudiante")
    libro=models.ForeignKey(Libro, on_delete=models.CASCADE, verbose_name="Libro")
    tipo = models.CharField(max_length=7, choices=TIPO_CHOICES, verbose_name="Tipo de Prestamo")
    cantidad = models.PositiveIntegerField(validators=[MinValueValidator(1)],verbose_name="Cantidad del libro")
    limite=models.DateField(editable=False, verbose_name="Fecha límite de Devolución")
    fecha=models.DateTimeField(auto_now_add=True)
    funcionario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, editable=False)
    penalizacion = models.CharField(max_length=50, default='Sin penalización')
    devuelto = models.BooleanField(default=False, editable=False, verbose_name="Devuetlo")
    
    def __str__(self):
        if self.funcionario:
            return f"Prestamo #{self.id} - Libro: {self.libro.cantidadint} - Funcionario: {self.funcionario.username} - Fecha de devolución: {self.limite}"
        else:
            return f"Prestamo #{self.id} - Funcionario: No asignado - Fecha de devolución: {self.limite}"

    class Meta:
        verbose_name='prestamo'
        verbose_name_plural='prestamos'
    
    def save(self, *args, **kwargs):
        if not self.id:  # Verifica si el objeto es nuevo
            self.limite = self._calculate_fecha_devolucion()
            self.funcionario = self._get_current_user()
        
        super(Prestamo, self).save(*args, **kwargs)
        self.actualizar_cantidad_libro()
        self.actualizar_estatus()
        self.aumentar_devoluciones()
        
    def actualizar_cantidad_libro(self):
        
        if self.devuelto:
            return
        
        if self.tipo == 'Interno':
            self.libro.cantidadint -= self.cantidad
            self.libro.save()
        else:
            self.libro.cantidadext -= self.cantidad
            self.libro.save()
            
    def aumentar_devoluciones(self):
        
        if self.devuelto:
            self.estudiante.devoluciones += 1
            self.estudiante.save() 
            
    def actualizar_estatus(self):
        
        if self.penalizacion == 'Penalización semanal':
            self.estudiante.estatus = 'Deshabilitado'
            self.estudiante.save()
        else:
            self.estudiante.estatus = 'Habilitado'
            self.estudiante.save()

    def _get_current_user(self):
        User = get_user_model()
        try:
            return User.objects.get(username=self._get_request_username())
        except User.DoesNotExist:
            return None

    def _get_request_username(self):
        request = self._get_request()
        if request and request.user.is_authenticated:
            return request.user.username
        return None

    def _get_request(self):
        import inspect
        frame = inspect.currentframe()
        while frame:
            if 'request' in frame.f_locals:
                return frame.f_locals['request']
            frame = frame.f_back
        return None  
    
    def _calculate_fecha_devolucion(self):
        if self.tipo == 'Interno':
            return datetime.today().date()
        
        today = datetime.today().date()
        days_ahead = 7

        while days_ahead > 0:
            today += timedelta(days=1)
            days_ahead -= 1
        # Omitir fines de semana (días 5 y 6 corresponden a sábado y domingo)
        # Si la fecha de devolución cae en sábado, sumar dos días adicionales
        if today.weekday() == 5:
            today += timedelta(days=2)

        # Si la fecha de devolución cae en domingo, sumar un día adicional
        if today.weekday() == 6:
            today += timedelta(days=1)
        return today    
    
