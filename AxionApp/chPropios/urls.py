from django.contrib.auth.decorators import login_required
from django.urls import path
from chPropios.views import *

urlpatterns = [
    path('detalle_ch/<int:id>', login_required(detalle_chPropio), name='detalleCheque'),
    path('agregar_ch/', login_required(agregar_ChPropio), name='agregarCheque'),
    path('editar_ch/<int:id>', login_required(editar_ChPropio), name='editarCheque'),
    path('eliminar_ch/<int:id>', login_required(eliminar_ChPropio), name='eliminarCheque'),
]
