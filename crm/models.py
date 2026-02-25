from django.db import models

# Create your models here.
from django.db import models

class Cliente(models.Model):
    nombre_completo = models.CharField(max_length=100)
    empresa = models.CharField(max_length=100, blank=True, null=True)
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    ciudad = models.CharField(max_length=50, blank=True, null=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre_completo

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

class Oportunidad(models.Model):
    ESTADO_CHOICES = [
        ('nuevo', 'Nuevo'),
        ('en_seguimiento', 'En seguimiento'),
        ('contactado', 'Contactado'),
        ('en_negociacion', 'En negociación'),
        ('cerrado', 'Cerrado'),
    ]

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    descripcion = models.TextField()
    valor_estimado = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='nuevo')
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.cliente} - {self.estado}"

    class Meta:
        verbose_name = "Oportunidad"
        verbose_name_plural = "Oportunidades"