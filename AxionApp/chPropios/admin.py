from django.contrib import admin
from chPropios.models import chPropio


class chPropioAdmin(admin.ModelAdmin):
    list_display = ('id', 'proveedor', 'banco', 'numCh', 'fechaVto', 'monto')  # modo tabla en admin
    search_fields = ('banco', 'numCh', 'monto')  # barra de busqueda
    list_filter = ('fechaVto', 'proveedor')  # filtros a la derecha
    raw_id_fields = ('proveedor',) # buscador de clave foraneas
    ordering = ('fechaVto',) # orden descendiente , para orden ascendiente: '-fechaVto'
    # fields = ('fechaVto', 'monto', 'proveedor', 'banco', 'numCh') # orden en que aparecen los campos en el formulario de carga
    # readonly_fields=('fechaCarga','otro') # para decir que son solo campos de solo lectura

# Register your models here.
admin.site.register(chPropio, chPropioAdmin)
