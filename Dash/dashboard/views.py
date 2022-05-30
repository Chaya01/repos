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

class detalle_usuario(DetailView):
    model = Usuarios

class crear_usuario(CreateView):
    model = Usuarios
    exito_url = reverse_lazy('directorio:list')
    campos = ['rut', 'nombre','area', 'correo', 'telefono']

class actualizar_usuario(UpdateView):
    model = Usuarios
    exito_url = reverse_lazy('directorio:list')
    campos = ['rut', 'nombre','area', 'correo', 'telefono']

class borrar_usuario(DeleteView):
    model = Usuarios
    exito_url = reverse_lazy('directorio:list')
    


# Create your views here.
