from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


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

# Create your views here.
