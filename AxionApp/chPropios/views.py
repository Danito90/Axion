from django.shortcuts import render, get_object_or_404, redirect
from datetime import datetime, date

# Create your views here.
from chPropios.forms import chPropioForm
from chPropios.models import chPropio, Proveedor


def detalle_chPropio(request, id):
    chP = get_object_or_404(chPropio, pk=id)
    vto = date.today()
    return render(request, 'chPropio/detalle_ch.html', {'detalleCh': chP, 'vencimiento': vto})


# chPropioForm = modelform_factory(chPropio, exclude=[])

def agregar_ChPropio(request):
    if request.method == 'POST':
        formCh = chPropioForm(request.POST)  # obtenemos los datos del formulario
        if formCh.is_valid():
            formCh.save()
            return redirect("/agregar_ch/?valido")  # volvemos a la misma pagina pasamos el parametro y enviamos mensaje
    else:
        formCh = chPropioForm()
    return render(request, 'chPropio/agregar_ch.html', {'FormCh': formCh})


def editar_ChPropio(request, id):
    chP = get_object_or_404(chPropio, pk=id)
    if request.method == 'POST':
        formCh = chPropioForm(request.POST, instance=chP)  # obtenemos los datos del formulario
        if formCh.is_valid():
            formCh.save()
            return redirect('index')
    else:
        formCh = chPropioForm(instance=chP)
    return render(request, 'chPropio/editar_ch.html', {'FormCh': formCh})


def eliminar_ChPropio(request, id):
    chP = get_object_or_404(chPropio, pk=id)
    if chP:
        chP.delete()
    return redirect('index')
