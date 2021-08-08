from django.urls import path
from proveedor.views import agregar_Prov, cuenta_Prov

urlpatterns = [
    path('agregar_prov/', agregar_Prov, name='agregarProveedor'),
    path('cuenta_prov/<int:id>', cuenta_Prov, name='cuentaProveedor'),
]
