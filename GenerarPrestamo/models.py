from django.db import models
from AdministrarLibros.models import Libro
from AdministrarEstudiantes.models import Estudiante
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

# Create your models here.

class Prestamo(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="Nota de Prestamo")
    estudiante=models.ForeignKey(Estudiante, on_delete=models.CASCADE, verbose_name="Estudiante")
    libro=models.ForeignKey(Libro, on_delete=models.CASCADE, verbose_name="Libro")
    limite=models.DateField(verbose_name="Fecha límite de entrega")
    fecha=models.DateTimeField(auto_now_add=True)
    funcionario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, editable=False)
    
    def __str__(self):
        if self.funcionario:
            return f"Prestamo #{self.id} - Funcionario: {self.funcionario.username}"
        else:
            return f"Prestamo #{self.id} - Funcionario: No asignado"

    class Meta:
        verbose_name='prestamo'
        verbose_name_plural='prestamos'
    
    def save(self, *args, **kwargs):
        if not self.id:  # Verifica si el objeto es nuevo
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
    
