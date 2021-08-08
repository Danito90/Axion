from django.contrib import admin

# Register your models here.
from proveedor.models import Proveedor


class proveedorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')  # modo tabla en admin
    search_fields = ('nombre', 'cuit')  # barra de busqueda


admin.site.register(Proveedor, proveedorAdmin)
