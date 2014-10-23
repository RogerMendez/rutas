#encoding:utf-8
from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse, Http404
from django.template import RequestContext
from django.template.loader import render_to_string
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import permission_required

from rutas.log_admin import admin_log_addition, admin_log_change
from rutas.reportes import generar_pdf

from asociaciones.models import Asociacion
from lineas.models import Linea
from lineas.form import LineaForm

@permission_required('lineas.add_linea', login_url='/login')
def mis_lineas(request):
    asociacion = Asociacion.objects.get(usuario = request.user)
    lineas = Linea.objects.filter(asociacion = asociacion)
    return render(request, 'lineas/mis_lineas.html',{
        'lineas':lineas,
    })

@permission_required('lineas.add_linea', login_url='/login')
def add_mi_linea(request):
    asoci = Asociacion.objects.get(usuario = request.user)
    if request.method == 'POST':
        formulario = LineaForm(request.POST)
        if formulario.is_valid():
            l = formulario.save()
            l.asociacion = asoci
            l.save()
            admin_log_addition(request, l, 'Linea Creada')
            admin_log_change(request, asoci, 'Linea Creada')
            sms = "Linea <strong>%s</strong> Creada Correctamente"% (l.nombre)
            messages.success(request, sms)
            return HttpResponseRedirect(reverse(mis_lineas))
    else:
        formulario = LineaForm()
    return render(request, 'lineas/new_linea.html',{
        'formulario':formulario,
    })

def mapa(request):
    return render(request, 'lineas/mapa.html',{})