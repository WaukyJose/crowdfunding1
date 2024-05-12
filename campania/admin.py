from django.contrib import admin

# Register your models here.
from campania.models import Categoria, Campania, Donacion

admin.site.site_header = "Administrador de Crowfunding"


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "slug", "fecha_registro", "fecha_ult_act")


@admin.register(Campania)
class CampaniaAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "nombre",
        "descripcion",
        "beneficiario",
        "monto_recaudar",
        "monto_recaudado",
        "fecha_inicio",
        "fecha_cierre",
        "estado",
        "fecha_registro",
        "fecha_ult_act",
    )


@admin.register(Donacion)
class DonacionAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "usuario",
        "campania",
        "monto",
        "fecha_registro",
        "fecha_ult_act",
    )

