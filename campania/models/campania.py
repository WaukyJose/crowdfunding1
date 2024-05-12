from django.db import models
from .categoria import Categoria

# other fields...


class Campania(models.Model):
    categorias = models.ManyToManyField(Categoria, related_name="campanias")
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True, null=True)
    imagen = models.ImageField(upload_to="imagenes/")
    beneficiario = models.CharField(max_length=150)
    monto_recaudar = models.DecimalField(max_digits=9, decimal_places=2)
    monto_recaudado = models.DecimalField(max_digits=9, decimal_places=2)
    fecha_inicio = models.DateTimeField()
    fecha_cierre = models.DateTimeField()
    estado = models.BooleanField()
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_ult_act = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self) -> str:
        return f"{self.nombre} ({self.id})"

    class Meta:
        db_table = "st_campania"
        verbose_name = "Campaña"
        verbose_name_plural = "Campañas"
