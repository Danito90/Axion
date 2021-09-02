from Empresa.models import Empresa
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.db.models import Sum
from django.shortcuts import render

# Create your views here.
from chPropios.models import chPropio
from datetime import datetime, date


# @login_required #esto es para que solo se pueda acceder con el login... pero podemos hacerlo desde las urls directamente
def bienvenido(request):
    no_cheques = chPropio.objects.filter(pagado=False).count()  # cuenta cheques pagados
    cheques = chPropio.objects.all().filter(empresa__user__id=request.user.id).order_by('pagado','fechaVto','monto')
    # .filter(empresa__user__id=request.user.id) filtro por empresa-usuario-usuario logeado
    #.filter(empresa__user__id=1) filtra por usuario id 1
    #filtra empresa 1 -2  ... .filter(empresa__in=[1, 2,])
    vto = date.today()
    total = chPropio.objects.filter(pagado=False).aggregate(total=Sum('monto'))[
        'total']  # obtener la suma de la columna monto
    # obtener la suma de la columna monto

    return render(request, 'bienvenido.html',
                  {'no_cheques': no_cheques, 'cheques_all': cheques, 'vencimiento': vto, 'total': total})
