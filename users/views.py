#encoding:utf-8
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, AdminPasswordChangeForm, UserCreationForm
from django.contrib.auth.decorators import login_required

from users.form import EmailForm, PerfilForm

def home(request):
    return render(request,'base.html',{})

def new_user(request):
    if request.method == 'POST':
        formuser = UserCreationForm(request.POST)
        formemail = EmailForm(request.POST)
        if formemail.is_valid() and formuser.is_valid() :
            u = formuser.save()
            u.email = formemail.cleaned_data['email']
            u.save()

            msm = "Su Cuenta fue creada Correctamente"
            messages.add_message(request, messages.INFO, msm)
            return HttpResponseRedirect('/')
    else:
        formuser = UserCreationForm()
        formemail = EmailForm()
    return render(request, 'users/new_user.html', {
        'formuser':formuser,
        'formemail':formemail,
    })


def iniciar_sesion(request):
    if not request.user.is_anonymous():
        return HttpResponseRedirect(reverse(privado))
    if request.method == 'POST':
        formulario = AuthenticationForm(request.POST)
        if formulario.is_valid:
            usuario = request.POST['username']
            clave = request.POST['password']
            acceso = authenticate(username=usuario, password=clave)
            if acceso is not None:
                if acceso.is_active:
                    login(request, acceso)
                    sms = 'Sesión Iniciada Correctamente'
                    messages.success(request, sms, )
                    if 'next' in request.GET:
                        return HttpResponseRedirect(str(request.GET['next']))
                    else:
                        return HttpResponseRedirect(reverse(privado))
                else:
                    sms = 'Su Cuenta de Usuario No Esta Activada'
                    messages.warning(request, sms,)
                    return HttpResponseRedirect(reverse(iniciar_sesion))
            else:
                sms = 'Usted No Es Usuario Registrado'
                #messages.warning(request, sms,)
                messages.error(request, sms, 'danger')
                #messages.info(request, sms, )
                #messages.success(request, sms, )
                return HttpResponseRedirect(reverse(iniciar_sesion))
    else:
        formulario = AuthenticationForm()
    return render(request, 'users/login.html', {
        'formulario':formulario,
    })

@login_required(login_url='/login')
def cerrar_sesion(request):
    logout(request)
    sms = 'Sesión Terminada Correctamente'
    messages.add_message(request, messages.INFO, sms)
    return HttpResponseRedirect('/')

@login_required(login_url='/login')
def edit_perfil(request):
    if request.method == 'POST':
        formulario = PerfilForm(request.POST, instance=request.user)
        if formulario.is_valid():
            formulario.save()
            sms = "Perfil Completado Corrctamente"
            messages.success(request, sms)
            return HttpResponseRedirect(reverse(privado))
    else:
        formulario = PerfilForm(instance=request.user)
    return render(request, 'users/edit_perfil.html',{
        'formulario':formulario,
    })

@login_required(login_url='/login')
def privado(request):
    #empleado = Empleado.objects.get(usuario = request.user)
    return render(request, 'users/index.html', {
        #'empleado':empleado,
    })

@login_required(login_url='/login')
def cambiar_password(request):
    if request.method == 'POST' :
        formulario = AdminPasswordChangeForm(user=request.user, data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect(reverse(iniciar_sesion))
    else:
        formulario = AdminPasswordChangeForm(user=request.user)
    return  render(request, 'users/reset_pass.html', {
        'formulario' :formulario,
        })


