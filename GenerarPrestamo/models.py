from django.db import models
from AdministrarLibros.models import Libro
from AdministrarEstudiantes.models import Estudiante
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from datetime import datetime, timedelta

# Create your models here.

class Prestamo(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="Nota de Prestamo")
    estudiante=models.ForeignKey(Estudiante, on_delete=models.CASCADE, verbose_name="Estudiante")
    libro=models.ForeignKey(Libro, on_delete=models.CASCADE, verbose_name="Libro")
    limite=models.DateField(editable=False, verbose_name="Fecha límite de Devolución")
    fecha=models.DateTimeField(auto_now_add=True)
    funcionario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, editable=False)
    
    def __str__(self):
        if self.funcionario:
            return f"Prestamo #{self.id} - Funcionario: {self.funcionario.username} - Fecha de devolución: {self.limite}"
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
    
