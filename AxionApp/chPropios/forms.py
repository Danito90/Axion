from django.forms import ModelForm, SelectDateWidget

from chPropios.choices import BANCOS
from chPropios.models import chPropio
from django import forms



class chPropioForm(ModelForm, forms.Form):
    #banco = forms.ChoiceField(choices=BANCOS, required=True, label="Banco")  # borra configuracion de model aca

    # fechaVto=  forms.DateField(widget=SelectDateWidget()) #borra configuracion de model aca

    # # opcion fecha en formulario
    # def __init__(self, *args, **kwargs):
    #     super(chPropioForm, self).__init__(*args, **kwargs)
    #     self.fields['fechaCarga'].widget = SelectDateWidget()  # ponerlo asi
    #     self.fields['fechaVto'].widget = SelectDateWidget()
    #     self.fields['monto'].initial = 123 #valores iniciales

    class Meta:
        model = chPropio
        # indicamos los campos a utilizar
        # fields= campos a utilizar
        # '__all__' : todos los campos
        fields = '__all__'
        # indicamos el tipo de campo del formulario de tipo persona
        # widgets : es un diccionario donde podemos indicar en el el tipo de dato pero a nivel html que va a
        # tener cada uno de nuestros campos
        # attrs={} significa atributo
        # attrs={} diccionario con el tipo de dato, se pueden agregar mas validaciones
        widgets = {
            'fechaCarga': forms.DateInput(attrs={'class': 'datepicker'}),
            'fechaVto': forms.DateInput(attrs={'class': 'datepicker'}),
        }

        labels = {
            'proveedor': 'Proveedor',
            'numCh': 'Numero de Cheque',
            'fechaCarga': 'Fecha de carga',
            'fechaVto': 'Vencimiento',
            'monto': 'Monto',
            'pagado': 'Pagado?',
        }
