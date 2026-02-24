from django.db import models

# Create your models here.

class Componente(models.Model):
    nombre = models.CharField(max_length=100)
    codigo_qr = models.CharField(max_length=50)
    cantidad = models.IntegerField()
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre