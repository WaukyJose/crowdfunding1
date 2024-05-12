from django.db import models
from django.contrib.auth.models import User
from .campania import Campania


class Donacion(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    campania = models.ForeignKey(Campania, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=12, decimal_places=2)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_ult_act = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"({self.id})"

    class Meta:
        db_table = "st_donacion"
        verbose_name = "Donación"
        verbose_name_plural = "Donaciones"
