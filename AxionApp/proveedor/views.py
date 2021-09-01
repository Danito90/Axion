from django.db.models import Sum
from django.forms import modelform_factory
from django.shortcuts import render, redirect
from datetime import datetime, date

# Create your views here.
from chPropios.models import chPropio
from proveedor.models import Proveedor
from Empresa.models import Empresa

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


def cuenta_Prov(request, filtro, id):
    if filtro == 0:
        proveedor_filtrado = Proveedor.objects.get(id=id)
        cheques = chPropio.objects.filter(proveedor=proveedor_filtrado).order_by('monto', 'fechaVto')
        vto = date.today()
        no_cheques = chPropio.objects.filter(pagado=False, proveedor=proveedor_filtrado).count()
        total = chPropio.objects.filter(pagado=False, proveedor=proveedor_filtrado).aggregate(total=Sum('monto'))[
            'total']  # obtener la suma de la columna monto
        return render(request, 'cuenta_prov.html',
                    {'no_cheques': no_cheques, 'cheques_all': cheques, 'nombre': proveedor_filtrado.nombre,'id': proveedor_filtrado.id,
                    'vencimiento': vto, 'total': total})
    elif filtro == 1:
        empresa_filtrada = Empresa.objects.get(id=id)
        cheques = chPropio.objects.filter(empresa=empresa_filtrada).order_by('monto', 'fechaVto')
        vto = date.today()
        no_cheques = chPropio.objects.filter(pagado=False, empresa=empresa_filtrada).count()
        total = chPropio.objects.filter(pagado=False, empresa=empresa_filtrada).aggregate(total=Sum('monto'))[
        'total']  # obtener la suma de la columna monto
        return render(request, 'cuenta_prov.html',
                  {'no_cheques': no_cheques, 'cheques_all': cheques, 'nombre': empresa_filtrada.razonSocial,'id': empresa_filtrada.id,
                   'vencimiento': vto, 'total': total})
