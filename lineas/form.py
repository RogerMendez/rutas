from django.forms import ModelForm

from lineas.models import Linea

class LineaForm(ModelForm):
    class Meta:
        model = Linea
        exclude = ['asociacion']