from django.contrib import admin

from gestionPedidos.models import Cliente, Articulo, Pedido


# Register your models here.

class ClaseAdminCliente(admin.ModelAdmin):
    list_display = ("nombre", "direccion", "tfono")
    search_fields = ("nombre", "tfono")


class ClaseAdminArticulo(admin.ModelAdmin):
    list_filter = ("seccion",)


class ClaseAdminPedido(admin.ModelAdmin):
    list_display = ("numPedido", "fechaPedido")
    list_filter = ("fechaPedido",)
    date_hierarchy = "fechaPedido"


admin.site.register(Cliente, ClaseAdminCliente)
admin.site.register(Articulo, ClaseAdminArticulo)
admin.site.register(Pedido, ClaseAdminPedido)
