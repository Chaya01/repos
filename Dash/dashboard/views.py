from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from pkg_resources import empty_provider
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from rest_framework.permissions import AllowAny
from .forms import UserForm
#from dashboard.models import 
from .models import Usuarios

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

### CRUD USUARIOS ###
#@login_required
def listar_usuarios(request):
    """"
    Listado de usuarios
    """
    ctx = {}
    listado_usuarios = Usuarios.objects.all()
    paginator = Paginator(listado_usuarios,10)

    page = request.GET.get('page')
    try:
        d_list = paginator.page(page)
    except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            d_list = paginator.page(1)
    except EmptyPage:
        #If page is out of range (e.g. 9999), deliver last page of results.
            d_list = paginator.page(paginator.num_pages)

    ctx['Usuarios'] = d_list

    return render(
        request,
        'directorio/usuarios/mostrar_usuarios.html',
        ctx
    )

# Create your views here.
