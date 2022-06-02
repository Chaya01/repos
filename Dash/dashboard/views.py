from audioop import reverse
from re import U
from typing import List
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from .forms import nombre_usuario
from django.views import View
from .models import Usuarios
from .forms import *
from . import views
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (CreateView,UpdateView,DeleteView)

#@login_required
#def inicio(request):
#    """
#     Página inicial del sitio
#    :param request: Django request
#    :return: Html
#    """
#    ctx = {}
#
#    return render(
#        request,
#        'directorio/inicio.html',
#        ctx
#    )

class index(ListView):
    model = Usuarios
    template_name = 'dashboard/index.html'

###### CRUD USUARIO ######

class detalle_usuario(DetailView):
    model = Usuarios
    template_name = 'dashboard/crud/user_detail.html'

class crear_usuario(CreateView):
    model = Usuarios
    form_class = usuario_form
    #fields = ['rut','nombre','apellido','area','correo','telefono']
    template_name = 'dashboard/crud/form.html'
    success_url = reverse_lazy('dashboard:index')

    #validamos que el formulario sea valido
    def form_valid(self, form):
        rut = form.cleaned_data['rut']
        nombre = form.cleaned_data['nombre']
        apellido = form.cleaned_data['apellido']
        a = re.search("[a-z]$",nombre) #validar nombre
        b = re.search("[a-z]$",apellido) #validar apellido
        x = re.search("[0-9]{8}[0-9kK]{1}$", rut) #validar rut

        if not x:
            form.add_error('rut', 'rut invalido')
            return self.form_invalid(form)
        elif not a:
            form.add_error('nombre', 'el nombre solo debe contener caracteres alfanumericos')
            return self.form_invalid(form)
        elif not b:
            form.add_error('apellido','el apellido solo debe contener caracteres alfanumericos')
            return self.form_invalid(form)
        return super(crear_usuario, self).form_valid(form)

class actualizar_usuario(UpdateView):
    model = Usuarios
    form_class = usuario_form
    template_name = 'dashboard/crud/update.html'
    success_url = reverse_lazy('dashboard:index')
    #fields = ['rut', 'nombre','apellido','area', 'correo', 'telefono']

    #validamos que el formulario sea valido
    def form_valid(self, form):
        rut = form.cleaned_data['rut']
        nombre = form.cleaned_data['nombre']
        apellido = form.cleaned_data['apellido']
        a = re.search("[a-z]$",nombre) #validar nombre
        b = re.search("[a-z]$",apellido) #validar apellido
        x = re.search("[0-9]{8}[0-9kK]{1}$", rut) #validar rut

        if not x:
            form.add_error('rut', 'rut invalido')
            return self.form_invalid(form)
        elif not a:
            form.add_error('nombre', 'el nombre solo debe contener caracteres alfanumericos')
            return self.form_invalid(form)
        elif not b:
            form.add_error('apellido','el apellido solo debe contener caracteres alfanumericos')
            return self.form_invalid(form)
        return super(actualizar_usuario, self).form_valid(form)

class borrar_usuario(DeleteView):
    model = Usuarios
    template_name = 'dashboard/crud/delete.html'
    success_url = reverse_lazy('dashboard:index')
    
##### CRUD DEPARTAMENTOS #####

class crear_departamento(CreateView):
    model = Departamentos
    form_class = departamento_form
    template_name = 'dashboard/crud/form.html'
    success_url = reverse_lazy('dashboard:index')

    #def form_valid(self,form):

class actualizar_departamento(UpdateView):
    model = Departamentos
    form_class = departamento_form
    template_name = 'dashboard/crud/update.html'
    success_url = reverse_lazy('dashboard:index')

class detalle_departamento(DetailView):
    model = Departamentos
    form_class = departamento_form
    template_name = ('dashboard/crud/departamento_detail.html')
    succes_url = reverse_lazy('dashboard:index')
# Create your views here.
