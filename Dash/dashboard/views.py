from audioop import reverse
from re import U
from typing import List
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from .forms import nombre_usuario
from django.views import View
from .models import Usuarios
from .forms import *
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

#def obtener_nombre(request):
#    if request.method == 'POST':
#        form = nombre_usuario(request.POST)
#        if form.is_valid():
#            return HttpResponseRedirect ('/gracias/')
#    else:
#        form = nombre_usuario()
#    return render(request, 'nombre.html', {'form': form})

#class mi_vista(View):
#    def get(self, request):
#        form = nombre_usuario(request.POST)
#        if form.is_valid():
#            return HttpResponseRedirect ('/gracias/')
#        else:
#            form = nombre_usuario()
#        return render(request, '/directorio/nombre.html', {'form': form})

class listado(ListView):
    model = Usuarios
    template_name = 'dashboard/listado.html'

class detalle_usuario(DetailView):
    model = Usuarios
    template_name = 'dashboard/usuario_detail.html'


class crear_usuario(CreateView):
    model = Usuarios
    form_class = usuario_form
    template_name = 'dashboard/usuario_form.html'
    success_url = reverse_lazy('dashboard:list')

class actualizar_usuario(UpdateView):
    model = Usuarios
    form_class = usuario_form
    template_name = 'dashboard/usuario_form.html'
    success_url = reverse_lazy('dashboard:list')
    fields = ['rut', 'nombre','area', 'correo', 'telefono']

class borrar_usuario(DeleteView):
    model = Usuarios
    success_url = reverse_lazy('dashboard:list')
    


# Create your views here.
