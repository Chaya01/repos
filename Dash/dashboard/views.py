from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from .forms import nombre_usuario


#@login_required
def inicio(request):
    """
     Página inicial del sitio
    :param request: Django request
    :return: Html
    """
    ctx = {}

    return render(
        request,
        'directorio/inicio.html',
        ctx
    )

def obtener_nombre(request):
    if request.method == 'POST':
        form = nombre_usuario(request.POST)
        if form.is_valid():
            return HttpResponseRedirect ('/gracias/')
    else:
        form = nombre_usuario()
    return render(request, 'nombre.html', {'form': form})

# Create your views here.
