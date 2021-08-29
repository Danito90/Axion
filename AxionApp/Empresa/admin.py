from django.contrib import admin
from Empresa.models import Empresa

# Register your models here.
class empresaAdmin(admin.ModelAdmin):
    list_display = ('id','razonSocial', 'cuit',)  # modo tabla en admin
    search_fields = ('razonSocial', 'cuit', 'user')  # barra de busqueda


admin.site.register(Empresa, empresaAdmin)