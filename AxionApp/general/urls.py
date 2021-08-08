from django.contrib.auth.decorators import login_required
from django.urls import path

from general.views import bienvenido

urlpatterns = [
    path('', login_required(bienvenido), name='index'),
]
