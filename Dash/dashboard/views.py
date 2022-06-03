from audioop import reverse
from re import U
from tokenize import Single
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
    context_object_name = 'index'
    template_name = 'dashboard/index.html'
    queryset = Usuarios.objects.all()

    def get_context_data(self, **kwargs):
        context = super(index, self).get_context_data(**kwargs)
        context['Usuarios'] = Usuarios.objects.all()
        context['Departamentos'] = Departamentos.objects.all()
        context['Num_telefono'] = Num_telefono.objects.all()

        return context
        #return super().get_context_data(**kwargs)

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

    def form_valid(self,form):
        area = form.cleaned_data['area']
        sucursal = form.cleaned_data['sucursal']
        a = re.search("[a-z]$", area) #validar area
        b = re.search("[a-z]$", sucursal)#validar sucursal
        if not a:
            form.add_error('area', 'El area solo debe contener caracteres alfanumericos')
            return self.form_invalid(form)
        elif not b:
            form.add_error('sucursal','La sucursal solo debe contener caracteres alfanumericos')
            return self.form_invalid(form)
        return super(crear_departamento, self).form_valid(form)

class actualizar_departamento (UpdateView):
    model = Departamentos
    form_class = departamento_form
    template_name = 'dashboard/crud/update.html'
    success_url = reverse_lazy('dashboard:index')

    def form_valid(self,form):
        area = form.cleaned_data['area']
        sucursal = form.cleaned_data['sucursal']
        a = re.search("[a-z]$", area) #validar area
        b = re.search("[a-z]$", sucursal)#validar sucursal
        if not a:
            form.add_error('area', 'El area solo debe contener caracteres alfanumericos')
            return self.form_invalid(form)
        elif not b:
            form.add_error('sucursal','La sucursal solo debe contener caracteres alfanumericos')
            return self.form_invalid(form)
        return super(actualizar_departamento, self).form_valid(form)

class detalle_departamento(DetailView):
    model = Departamentos
    template_name = ('dashboard/crud/departamento_detail.html')
    succes_url = reverse_lazy('dashboard:index')

class borrar_departamento(DeleteView):
    model = Departamentos
    template_name = 'dashboard/crud/delete.html'
    success_url = reverse_lazy('dashboard:index')

##### CRUD Num_telefono#####

class crear_telefono(CreateView):
    model = Num_telefono
    template_name = 'dashboard/crud/form.html'
    form_class = telefono_form
    success_url = reverse_lazy('dashboard:index')

    def form_valid(self,form):
        numero_tel = form.cleaned_data['numero_tel']
        a = re.search("[1-9]{9}$", numero_tel) #validar telefono
        if not a:
            form.add_error('numero_tel', 'El telefono debe contener 9 caracteres y solo deben ser numericos')
            return self.form_invalid(form)
        return super(crear_telefono, self).form_valid(form)

class actualizar_telefono(UpdateView):
    model = Num_telefono
    template_name = 'dashboard/crud/update.html'
    success_url = reverse_lazy('dashboard:index')
    form_class = telefono_form

class detalle_telefono(DetailView):
    model = Num_telefono
    template_name = 'dashboard/crud/telefono_detail.html'
    success_url = reverse_lazy('dashboard:index')

class borrar_telefono(DeleteView):
    model = Num_telefono
    template_name = 'dashboard/crud/delete.html'
    success_url = reverse_lazy('dashboard:index')

# Create your views here.
