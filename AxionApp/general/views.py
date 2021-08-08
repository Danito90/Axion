from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.shortcuts import render

# Create your views here.
from chPropios.models import chPropio
from datetime import datetime, date


# @login_required #esto es para que solo se pueda acceder con el login... pero podemos hacerlo desde las urls directamente
def bienvenido(request):
    no_cheques = chPropio.objects.filter(pagado=False).count()  # cuenta cheques pagados
    cheques = chPropio.objects.all().order_by('monto', 'fechaVto')
    vto = date.today()
    total = chPropio.objects.filter(pagado=False).aggregate(total=Sum('monto'))[
        'total']  # obtener la suma de la columna monto
    # obtener la suma de la columna monto

    return render(request, 'bienvenido.html',
                  {'no_cheques': no_cheques, 'cheques_all': cheques, 'vencimiento': vto, 'total': total})
