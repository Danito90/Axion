from django.db.models import Sum
from django.forms import modelform_factory
from django.shortcuts import render, redirect
from datetime import datetime, date

# Create your views here.
from chPropios.models import chPropio
from proveedor.models import Proveedor

FormularioProv = modelform_factory(Proveedor, exclude=[])


def agregar_Prov(request):
    if request.method == 'POST':
        formProv = FormularioProv(request.POST)  # obtenemos los datos del formulario
        if formProv.is_valid():
            formProv.save()
            return redirect('index')
    else:
        formProv = FormularioProv()
    return render(request, 'agregar_prov.html', {'FormProv': formProv})


def cuenta_Prov(request, id):
    proveedor_filtrado = Proveedor.objects.get(id=id)
    cheques = chPropio.objects.filter(proveedor=proveedor_filtrado).order_by('monto', 'fechaVto')
    vto = date.today()
    no_cheques = chPropio.objects.filter(pagado=False, proveedor=proveedor_filtrado).count()
    total = chPropio.objects.filter(pagado=False, proveedor=proveedor_filtrado).aggregate(total=Sum('monto'))[
        'total']  # obtener la suma de la columna monto
    return render(request, 'cuenta_prov.html',
                  {'no_cheques': no_cheques, 'cheques_all': cheques, 'proveedor': proveedor_filtrado,
                   'vencimiento': vto, 'total': total})
