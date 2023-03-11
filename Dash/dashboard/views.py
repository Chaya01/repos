from audioop import reverse
from re import U
from tokenize import Single
from typing import List
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
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

        return context
        #return super().get_context_data(**kwargs)

##### Paneles de acceso ####

class panel_usuarios(ListView):
    context_object_name = 'panel_usuarios'
    template_name = 'dashboard/panel_usuarios.html'
    paginate_by = 10
    queryset = Usuarios.objects.all()
    def get_context_data(self, **kwargs):
        context = super(panel_usuarios, self).get_context_data(**kwargs)
        context['Usuarios'] = Usuarios.objects.all()
        return context

class panel_departamentos(ListView):
    context_object_name = 'panel_departamentos'
    template_name = 'dashboard/panel_departamentos.html'
    paginate_by = 10
    queryset = Departamentos.objects.all()
    def get_context_data(self, **kwargs):
        context = super(panel_departamentos, self).get_context_data(**kwargs)
        context['Departamentos'] = Departamentos.objects.all()
        return context
    
class panel_telefonos(ListView):
    context_object_name = 'panel_telefonos'
    template_name = 'dashboard/panel_telefonos.html'
    paginate_by = 10
    queryset = Num_telefono.objects.all()
    def get_context_data(self, **kwargs):
        context = super(panel_telefonos, self).get_context_data(**kwargs)
        context['Num_telefono'] = Num_telefono.objects.all()
        return context

class panel_smartphones(ListView):
    context_object_name = 'panel_smartphones'
    template_name = 'dashboard/panel_smartphones.html'
    paginate_by = 10
    queryset = Smartphones.objects.all()
    def get_context_data(self, **kwargs):
        context = super(panel_smartphones, self).get_context_data(**kwargs)
        context['Smartphones'] = Smartphones.objects.all()
        return context

class panel_tablets(ListView):
    context_object_name = 'panel_tablets'
    template_name = 'dashboard/panel_tablets.html'
    paginate_by = 10
    queryset = Tablets.objects.all()
    def get_context_data(self, **kwargs):
        context = super(panel_tablets, self).get_context_data(**kwargs)
        context['Tablets'] = Tablets.objects.all()
        return context

class panel_notebooks(ListView):
    context_object_name = 'panel_notebooks'
    template_name = 'dashboard/panel_notebooks.html'
    paginate_by = 10
    queryset = Notebooks.objects.all()
    def get_context_data(self, **kwargs):
        context = super(panel_notebooks, self).get_context_data(**kwargs)
        context['Notebooks'] = Notebooks.objects.all()
        return context
    
class panel_camionetas(ListView):
    context_object_name = 'panel_camionetas'
    template_name = 'dashboard/panel_camionetas.html'
    paginate_by = 10
    queryset = Camionetas.objects.all()
    def get_context_data(self, **kwargs):
        context = super(panel_camionetas, self).get_context_data(**kwargs)
        context['Camionetas'] = Camionetas.objects.all()
        return context
    
class panel_asignacion(ListView):
    context_object_name = 'panel_asignacion'
    template_name = 'dashboard/panel_asignacion.html'
    paginate_by = 10
    queryset = Asignacion.objects.all()
    def get_context_data(self, **kwargs):
        context = super(panel_asignacion, self).get_context_data(**kwargs)
        context['Asignacion'] = Asignacion.objects.all()
        return context

###### CRUD USUARIO ######

class detalle_usuario(DetailView):
    model = Usuarios
    template_name = 'dashboard/crud/user_detail.html'

class crear_usuario(CreateView):
    model = Usuarios
    form_class = UsuarioForm
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
    form_class = UsuarioForm
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
    form_class = DepartamentoForm
    template_name = 'dashboard/crud/form.html'
    success_url = reverse_lazy('dashboard:panel_departamentos')

"""    def form_valid(self,form):
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
"""
class actualizar_departamento (UpdateView):
    model = Departamentos
    form_class = DepartamentoForm
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

##### CRUD Num_telefono #####

class crear_telefono(CreateView):
    model = Num_telefono
    template_name = 'dashboard/crud/form.html'
    form_class = TelefonoForm
    success_url = reverse_lazy('dashboard:panel_telefonos')

    def form_valid(self,form):
        numero_tel = form.cleaned_data['numero_tel']
        a = re.search("[0-9]{9}$", numero_tel) #validar telefono
        if not a:
            form.add_error('numero_tel', 'El telefono debe contener 9 caracteres y solo deben ser numericos')
            return self.form_invalid(form)
        return super(crear_telefono, self).form_valid(form)

class actualizar_telefono(UpdateView):
    model = Num_telefono
    template_name = 'dashboard/crud/update.html'    
    success_url = reverse_lazy('dashboard:index')
    form_class = TelefonoForm

    def form_valid(self,form):
        numero_tel = form.cleaned_data['numero_tel']
        a = re.search("[1-9]{9}$", numero_tel) #validar telefono
        if not a:
            form.add_error('numero_tel', 'El telefono debe contener 9 caracteres y solo deben ser numericos')
            return self.form_invalid(form)
        return super(crear_telefono, self).form_valid(form)

class detalle_telefono(DetailView):
    model = Num_telefono
    template_name = 'dashboard/crud/telefono_detail.html'
    success_url = reverse_lazy('dashboard:index')

class borrar_telefono(DeleteView):
    model = Num_telefono
    template_name = 'dashboard/crud/delete.html'
    success_url = reverse_lazy('dashboard:index')

### Crud Smartphones ###

class crear_smartphone(CreateView):
    model = Smartphones
    template_name = 'dashboard/crud/form.html'
    form_class = SmartphonesForm
    success_url = reverse_lazy('dashboard:panel_smartphones')

class actualizar_smartphone(UpdateView):
    model = Smartphones
    template_name = 'dashboard/crud/update.html'    
    success_url = reverse_lazy('dashboard:panel_smartphones')
    form_class = SmartphonesForm

class detalle_smartphone(DetailView):
    model = Smartphones
    template_name = 'dashboard/crud/smartphone_detail.html'
    success_url = reverse_lazy('dashboard:panel_smartphones')

class borrar_smartphone(DeleteView):
    model = Smartphones
    template_name = 'dashboard/crud/delete.html'
    success_url = reverse_lazy('dashboard:panel_smartphones')

### Crud Tablet ###

class crear_tablet(CreateView):
    model = Tablets
    template_name = 'dashboard/crud/form.html'
    form_class = TabletsForm
    success_url = reverse_lazy('dashboard:panel_tablets')

class actualizar_tablet(UpdateView):
    model = Tablets
    template_name = 'dashboard/crud/update.html'    
    success_url = reverse_lazy('dashboard:panel_tablets')
    form_class = TabletsForm

class detalle_tablet(DetailView):
    model = Tablets
    template_name = 'dashboard/crud/tablet_detail.html'
    success_url = reverse_lazy('dashboard:panel_tablet')

class borrar_tablet(DeleteView):
    model = Tablets
    template_name = 'dashboard/crud/delete.html'
    success_url = reverse_lazy('dashboard:panel_tablet')

#### Crud Notebook ###

class crear_notebook(CreateView):
    model = Notebooks
    template_name = 'dashboard/crud/form.html'
    form_class = NotebooksForm
    success_url = reverse_lazy('dashboard:panel_notebooks')

class actualizar_notebook(UpdateView):
    model = Notebooks
    template_name = 'dashboard/crud/update.html'    
    success_url = reverse_lazy('dashboard:panel_notebooks')
    form_class = NotebooksForm

class detalle_notebook(DetailView):
    model = Notebooks
    template_name = 'dashboard/crud/tablet_detail.html'
    success_url = reverse_lazy('dashboard:panel_notebooks')

class borrar_notebook(DeleteView):
    model = Notebooks
    template_name = 'dashboard/crud/delete.html'
    success_url = reverse_lazy('dashboard:panel_notebooks')

### Crud Camionetas ###

class crear_camioneta(CreateView):
    model = Camionetas
    template_name = 'dashboard/crud/form.html'
    form_class = CamionetasForm
    success_url = reverse_lazy('dashboard:panel_camionetas')

class actualizar_camioneta(UpdateView):
    model = Camionetas
    template_name = 'dashboard/crud/update.html'    
    success_url = reverse_lazy('dashboard:panel_camionetas')
    form_class = CamionetasForm

class detalle_camioneta(DetailView):
    model = Camionetas
    template_name = 'dashboard/crud/tablet_detail.html'
    success_url = reverse_lazy('dashboard:panel_camionetas')

class borrar_camioneta(DeleteView):
    model = Camionetas
    template_name = 'dashboard/crud/delete.html'
    success_url = reverse_lazy('dashboard:panel_camionetas')

### Crud asginacion ###

class crear_asignacion(CreateView):
    model = Asignacion
    template_name = 'dashboard/crud/form.html'
    form_class = AsignacionForm
    success_url = reverse_lazy('dashboard:panel_asignacion')

class actualizar_asignacion(UpdateView):
    model = Asignacion
    template_name = 'dashboard/crud/update.html'    
    success_url = reverse_lazy('dashboard:panel_asignacion')
    form_class = AsignacionForm

class detalle_asignacion(DetailView):
    model = Asignacion
    template_name = 'dashboard/crud/tablet_detail.html'
    success_url = reverse_lazy('dashboard:panel_asignacion')

class borrar_asignacion(DeleteView):
    model = Asignacion
    template_name = 'dashboard/crud/delete.html'
    success_url = reverse_lazy('dashboard:panel_asignacion')













##### Crud Series #####

#    class crear_serie(CreateView):
#    model = Series
#    form_class = series_form
#    template_name = 'dashboard/crud/form.html'
#    success_url = reverse_lazy('dashboard:index')

#class actualizar_serie(UpdateView):
#    model = Series
#    form_class = series_form
#    template_name = 'dashboard/crud/update.html'
#    success_url = reverse_lazy('dashboard:index')

#class detalle_serie(DetailView):
#    model = Series
#    template_name = 'dashboard/crud/serie_detail.html'
#    success_url = reverse_lazy('dashboard:index')

#class borrar_serie(DeleteView):
#    model = Series
#    template_name = 'dashboard/crud/delete.html'
#    success_url = reverse_lazy('dashboard:index')

# Create your views here.
