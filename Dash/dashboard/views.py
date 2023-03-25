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
from django.shortcuts import render
from .forms import *
from . import views
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (CreateView,UpdateView,DeleteView)
from django.shortcuts import get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


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

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("dashboard:index")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(
            request=request,
            template_name="dashboard/login.html",
            context={"login_form":form})

@method_decorator(login_required, name='dispatch' )
class index(ListView):  
    context_object_name = 'index'
    template_name = 'dashboard/index.html'
    queryset = Usuarios.objects.all()

    def get_context_data(self, **kwargs):
        context = super(index, self).get_context_data(**kwargs)
        context['Usuarios'] = Usuarios.objects.all()
        ### Contadores de Smartphones ###
        context['total_smartphones'] = Smartphones.objects.count()
        context['assigned_smartphones'] = Asignacion.objects.filter(smartphone_a__estado_telefono=True, vigente=True).count()
        context['unusable_smartphones'] = Smartphones.objects.filter(estado_telefono=False).count()
        context['available_smartphones'] = context['total_smartphones'] - context['assigned_smartphones'] - context ['unusable_smartphones']
        ###Contadores de Notebooks ####
        context['total_notebooks'] = Notebooks.objects.count()
        context['assigned_notebooks'] = Asignacion.objects.exclude(notebook_a=None).exclude(vigente=False).count()
        context['unusable_notebooks'] = Notebooks.objects.filter(estado_notebook=False).count()
        context['available_notebooks'] = context['total_notebooks'] - context['assigned_notebooks'] - context['unusable_notebooks']
        ### Contadores de Tablets###
        context['total_tablets'] = Tablets.objects.count()
        context['assigned_tablets'] = Asignacion.objects.exclude(tablet_a=None).exclude(vigente=False).count()
        context['unusable_tablets'] = Tablets.objects.filter(estado_tablet=False).count()
        context['available_tablets'] = context['total_tablets'] - context['assigned_tablets'] - context['unusable_tablets']
        ### Contadores de camionetas ###
        context['total_camionetas'] = Camionetas.objects.count()
        context['assigned_camionetas'] = Asignacion.objects.exclude(camionetas_a=None).exclude(vigente=False).count()
        context['unusable_camionetas'] = Camionetas.objects.filter(disponible=False).count()
        context['available_camionetas'] = context['total_camionetas'] - context['assigned_camionetas'] - context['unusable_camionetas']

        return context
        #return super().get_context_data(**kwargs)

##### Paneles de acceso ####

@method_decorator(login_required, name='dispatch')
class panel_usuarios(ListView):
    context_object_name = 'panel_usuarios'
    template_name = 'dashboard/panel_usuarios.html'
    paginate_by = 20
    search_form = SearchForm

    def get_queryset(self):
        queryset = Usuarios.objects.order_by('nombre')
        query = self.request.GET.get('query')
        if query:
            queryset = queryset.filter(
                Q(nombre__icontains=query) |
                Q(apellido__icontains=query) |
                Q(rut__icontains=query)
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super(panel_usuarios, self).get_context_data(**kwargs)
        context['search_form'] = self.search_form(self.request.GET or None)
        return context

@method_decorator(login_required, name='dispatch' )
class panel_departamentos(ListView):
    context_object_name = 'panel_departamentos'
    template_name = 'dashboard/panel_departamentos.html'
    paginate_by = 20
    search_form = SearchForm

    def get_queryset(self):
        queryset = Departamentos.objects.order_by('area')
        query = self.request.GET.get('query')
        if query:
            queryset = queryset.filter(
                Q(area__icontains=query) |
                Q(sucursal__icontains=query)
            )
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super(panel_departamentos, self).get_context_data(**kwargs)
        context['search_form'] = self.search_form(self.request.GET or None)
        return context
    
@method_decorator(login_required, name='dispatch' )

class panel_telefonos(ListView):
    context_object_name = 'panel_telefonos'
    template_name = 'dashboard/panel_telefonos.html'
    paginate_by = 20
    search_form = SearchForm
    
    def get_queryset(self):
        queryset = Num_telefono.objects.order_by('numero_tel')
        query = self.request.GET.get('query')
        if query:
            queryset = queryset.filter(
                Q(numero_tel__icontains=query) |
                Q(activo__icontains=query)
            )
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super(panel_telefonos, self).get_context_data(**kwargs)
        context['search_form'] = self.search_form(self.request.GET or None)
        return context

@method_decorator(login_required, name='dispatch' )
class panel_smartphones(ListView):
    context_object_name = 'panel_smartphones'
    template_name = 'dashboard/panel_smartphones.html'
    paginate_by = 20
    search_form = SearchForm

    def get_queryset(self):
        queryset = Smartphones.objects.order_by('serie_smartphone')
        query = self.request.GET.get('query')
        if query:
            queryset = queryset.filter(
                Q(serie_smartphone__icontains=query) |
                Q(modelo_smartphone__m_modelo__icontains=query)  |
                Q(modelo_smartphone__m_marca__marca__icontains=query) |
                Q(modelo_smartphone__m_param__nombre_param__icontains=query) |
                Q(imei1__icontains=query) |
                Q(imei2__icontains=query) |
                Q(estado_telefono__icontains=query)  
            )
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super(panel_smartphones, self).get_context_data(**kwargs)
        context['search_form'] = self.search_form(self.request.GET or None)
        return context
    
@method_decorator(login_required, name='dispatch' )
class panel_tablets(ListView):
    context_object_name = 'panel_tablets'
    template_name = 'dashboard/panel_tablets.html'
    paginate_by = 20
    search_form = SearchForm

    def get_queryset(self):
        queryset = Tablets.objects.order_by('serie_tablet')
        query = self.request.GET.get('query')
        if query:
            queryset = queryset.filter(
                Q(serie_tablet__icontains=query) |
                Q(modelo_tablet__m_modelo__icontains=query)  |
                Q(modelo_tablet__m_marca__marca__icontains=query)  |
                Q(modelo_tablet__m_param__nombre_param__icontains=query)  |
                Q(estado_tablet__icontains=query)  
            )
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super(panel_tablets, self).get_context_data(**kwargs)
        context['search_form'] = self.search_form(self.request.GET or None)
        return context

@method_decorator(login_required, name='dispatch' )
class panel_notebooks(ListView):
    context_object_name = 'panel_notebooks'
    template_name = 'dashboard/panel_notebooks.html'
    paginate_by = 20
    search_form = SearchForm

    def get_queryset(self):
        queryset = Notebooks.objects.order_by('serie_notebook')
        query = self.request.GET.get('query')
        if query:
            queryset = queryset.filter(
                Q(serie_notebook__icontains=query) |
                Q(modelo_notebook__m_modelo__icontains=query)  |
                Q(modelo_notebook__m_marca__marca__icontains=query)  |
                Q(modelo_notebook__m_procesador__modelo_p__icontains=query)  |
                Q(nram__icontains=query)  |
                Q(estado_notebook__icontains=query)

            )
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super(panel_notebooks, self).get_context_data(**kwargs)
        context['search_form'] = self.search_form(self.request.GET or None)
        return context

@method_decorator(login_required, name='dispatch' )    
class panel_camionetas(ListView):
    context_object_name = 'panel_camionetas'
    template_name = 'dashboard/panel_camionetas.html'
    paginate_by = 20
    search_form = SearchForm

    def get_queryset(self):
        queryset = Camionetas.objects.order_by('patente')
        query = self.request.GET.get('query')
        if query:
            queryset = queryset.filter(
                Q(patente__icontains=query) |
                Q(modelo_camioneta__m_modelo__icontains=query) |
                Q(modelo_camioneta__m_marca__marca__icontains=query) |
                Q(disponible__icontains=query) |
                Q(modalidad__icontains=query) |
                Q(vin__icontains=query)
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super(panel_camionetas, self).get_context_data(**kwargs)
        context['search_form'] = self.search_form(self.request.GET or None)
        return context
    
    """"
    def get_queryset(self):
        queryset = super().get_queryset()
        patente = self.request.GET.get('patente')
        sort_param = self.request.GET.get('sort')
        current_order = self.request.session.get('current_order', 'asc')  # get the current sorting order from the session, default to ascending order
        if sort_param == 'patente':
            if current_order == 'asc':
                queryset = queryset.order_by('patente')
                self.request.session['current_order'] = 'desc'
            else:
                queryset = queryset.order_by('-patente')
                self.request.session['current_order'] = 'asc'
        elif sort_param == 'modelo_camioneta':
            if current_order == 'asc':
                queryset = queryset.order_by('modelo_camioneta')
                self.request.session['current_order'] = 'desc'
            else:
                queryset = queryset.order_by('-modelo_camioneta')
                self.request.session['current_order'] = 'asc'
        elif sort_param == 'mantencion':
            if current_order == 'asc':
                queryset = queryset.order_by('mantencion')
                self.request.session['current_order'] = 'desc'
            else:
                queryset = queryset.order_by('-mantencion')
                self.request.session['current_order'] = 'asc'
        else:
            queryset = queryset.order_by('patente')
            self.request.session['current_order'] = 'asc'
        return queryset
"""
@method_decorator(login_required, name='dispatch' )   
class panel_asignacion(ListView):
    context_object_name = 'panel_asignacion'
    template_name = 'dashboard/panel_asignacion.html'
    paginate_by = 20
    search_form = SearchForm

    def get_queryset(self):
        queryset = Asignacion.objects.order_by('usuario')
        query = self.request.GET.get('query')
        if query:
            queryset = queryset.filter(
                Q(usuario__nombre__icontains=query) |
                Q(num__numero_tel__icontains=query) |
                Q(smartphone_a__modelo_smartphone__m_modelo__icontains=query) |
                Q(smartphone_a__modelo_smartphone__m_marca__marca__icontains=query) |
                Q(tablet_a__modelo_tablet__m_modelo__icontains=query) |
                Q(tablet_a__modelo_tablet__m_marca__marca__icontains=query) |
                Q(notebook_a__modelo_notebook__m_modelo__icontains=query) |
                Q(notebook_a__modelo_notebook__m_marca__marca__icontains=query) |
                Q(camionetas_a__modelo_camioneta__m_modelo__icontains=query) |
                Q(camionetas_a__modelo_camioneta__m_marca__marca__icontains=query) |
                Q(vigente__icontains=query)
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super(panel_asignacion, self).get_context_data(**kwargs)
        get_vigente_display = lambda asignacion: 'Vigente' if asignacion.vigente else 'No vigente'
        vigente_display_list = [get_vigente_display(asignacion) for asignacion in context['panel_asignacion']]
        context['vigente_display_list'] = vigente_display_list
        context['search_form'] = self.search_form(self.request.GET or None)
        return context
    
    # Define a lambda function to get the display value of 'vigente'
    # Use a list comprehension to get the display value of 'vigente' for each object
    # Add the 'vigente_display_list' to the context

@method_decorator(login_required, name='dispatch' )    
class panel_modelos(ListView):
    context_object_name = 'panel_modelos'
    template_name = 'dashboard/panel_modelos.html'
    paginate_by = 20
    search_form = SearchForm

    def get_queryset(self):
        queryset = Modelos.objects.order_by('m_marca')
        query = self.request.GET.get('query')
        if query:
            queryset = queryset.filter(
                Q(m_marca__marca__icontains=query) |
                Q(m_param__nombre_param__icontains=query)  |
                Q(m_modelo__icontains=query)  |
                Q(m_procesador__modelo_p__icontains=query) |
                Q(m_procesador__marca_procesador__icontains=query)
            )
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super(panel_modelos, self).get_context_data(**kwargs)
        context['search_form'] = self.search_form(self.request.GET or None)
        return context
    

@method_decorator(login_required, name='dispatch' )    
class panel_procesadores(ListView):
    context_object_name = 'panel_procesadores'
    template_name = 'dashboard/panel_procesadores.html'
    paginate_by = 20
    search_form = SearchForm

    def get_queryset(self):
        queryset = Procesador.objects.order_by('marca_procesador')
        query = self.request.GET.get('query')
        if query:
            queryset = queryset.filter(
                Q(marca_procesador__icontains=query) |
                Q(modelo_p__icontains=query)  |
                Q(ghz__icontains=query)  |
                Q(nucleos__icontains=query) |
                Q(año_mf__icontains=query)
            )
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super(panel_procesadores, self).get_context_data(**kwargs)
        context['search_form'] = self.search_form(self.request.GET or None)
        return context

@method_decorator(login_required, name='dispatch' )
class panel_marcas(ListView):
    context_object_name = 'panel_marcas'
    template_name = 'dashboard/panel_marcas.html'
    paginate_by = 20
    search_form = SearchForm

    def get_queryset(self):
        queryset = Marca.objects.order_by('marca')
        query = self.request.GET.get('query')
        if query:
            queryset = queryset.filter(
                Q(marca__icontains=query)
            )
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super(panel_marcas, self).get_context_data(**kwargs)
        context['search_form'] = self.search_form(self.request.GET or None)
        return context

@method_decorator(login_required, name='dispatch' )    
class panel_mantenciones(ListView):
    context_object_name = 'panel_mantencion'
    template_name = 'dashboard/panel_mantencion.html'
    paginate_by = 20
    search_form = SearchForm

    def get_queryset(self):
        queryset = Mantenciones.objects.order_by('m_patente')
        query = self.request.GET.get('query')
        if query:
            queryset = queryset.filter(
                Q(m_patente__patente__icontains=query)  |
                Q(m_kilometraje__icontains=query)  |
                Q(m_estado__icontains=query)  |
                Q(responsable__usuario__nombre__icontains=query) 
            )
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super(panel_mantenciones, self).get_context_data(**kwargs)
        context['search_form'] = self.search_form(self.request.GET or None)
        return context

@method_decorator(login_required, name='dispatch' )    
class listado_mantenciones(ListView):
    model = Mantenciones
    template_name = 'dashboard/listado_mantenciones.html'
    context_object_name = 'mantenciones'
    paginate_by = 20

    def get_queryset(self):
        camionetas_id = self.kwargs.get('pk')
        return Mantenciones.objects.filter(m_patente_id=camionetas_id)
"""    def get_queryset(self):
        # Retrieve the user ID from the URL parameter
        camionetas_id  = self.kwargs.get('pk')
#        print("User ID:", matricula_id) print query data

        # Return a queryset of all Cuotas objects that belong to the user
        return Mantenciones.objects.filter(m_patente_id=camionetas_id)
"""

@method_decorator(login_required, name='dispatch' )
class reporte(DetailView):
    model = Usuarios
    template_name = 'dashboard/crud/reporte_usuario.html'
    context_object_name= 'Usuarios'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        asignaciones = self.object.asignacion_set.all() # access all Asignacion objects related to the user
        context['asignaciones'] = list(asignaciones) # add the Asignacion objects to the context as a list
        return context
"""
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        asignacion = self.object.asignacion_set.first() # access the first Asignacion object related to the user
        if asignacion: # check if the user has any related Asignacion object
            context['notebook_a'] = asignacion.notebook_a # add the notebook_a object to the context
        elif asignacion :
            context['tablet_a'] = asignacion.tablet_a
        elif asignacion :
            context['smartphone_a'] = asignacion.smartphone_a
        return context
"""
"""
    def get_context_data(selfw, **kwargs):
        context = super().get_context_data(**kwargs)
        usuario = self.get_object()
        context['smartphones'] = usuario.asignacion_set.filter(smartphone_a__isnull=False).values_list('smartphone_a__modelo_smartphone__m_modelo', flat=True)
        context['smartphones'] = usuario.asignacion_set.filter(smartphone_a__isnull=False).values_list('smartphone_a__modelo_smartphone__m_modelo', flat=True)
        context['tablets'] = usuario.asignacion_set.filter(tablet_a__isnull=False).values_list('tablet_a__modelo_tablet__m_modelo', flat=True)
        context['notebooks'] = usuario.asignacion_set.filter(notebook_a__isnull=False).values_list('notebook_a__modelo_notebook__m_modelo', flat=True)
        context['camionetas'] = usuario.asignacion_set.filter(camionetas_a__isnull=False).values_list('camionetas_a__modelo_camioneta__m_modelo', flat=True)
        return context
"""
###### CRUD USUARIO ######

@method_decorator(login_required, name='dispatch' )
class detalle_usuario(DetailView):
    model = Usuarios
    template_name = 'dashboard/crud/user_detail.html'


@method_decorator(login_required, name='dispatch' )
class crear_usuario(CreateView):
    model = Usuarios
    form_class = UsuarioForm
    #fields = ['rut','nombre','apellido','area','correo','telefono']
    template_name = 'dashboard/crud/form.html'
    success_url = reverse_lazy('dashboard:panel_usuarios')

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
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_verbose_name'] = self.model._meta.verbose_name.title()
        return context

@method_decorator(login_required, name='dispatch' )
class actualizar_usuario(UpdateView):
    model = Usuarios
    form_class = UsuarioForm
    template_name = 'dashboard/crud/update.html'
    success_url = reverse_lazy('dashboard:panel_usuarios')
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

@method_decorator(login_required, name='dispatch' )
class borrar_usuario(DeleteView):
    model = Usuarios
    template_name = 'dashboard/crud/delete.html'
    success_url = reverse_lazy('dashboard:panel_usuarios')
    
##### CRUD DEPARTAMENTOS #####

@method_decorator(login_required, name='dispatch' )
class crear_departamento(CreateView):
    model = Departamentos
    form_class = DepartamentoForm
    template_name = 'dashboard/crud/form.html'
    success_url = reverse_lazy('dashboard:panel_departamentos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_verbose_name'] = self.model._meta.verbose_name.title()
        return context
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
@method_decorator(login_required, name='dispatch' )
class actualizar_departamento (UpdateView):
    model = Departamentos
    form_class = DepartamentoForm
    template_name = 'dashboard/crud/update.html'
    success_url = reverse_lazy('dashboard:panel_departamentos')

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

@method_decorator(login_required, name='dispatch' )
class detalle_departamento(DetailView):
    model = Departamentos
    template_name = ('dashboard/crud/departamento_detail.html')
    succes_url = reverse_lazy('dashboard:index')

@method_decorator(login_required, name='dispatch' )
class borrar_departamento(DeleteView):
    model = Departamentos
    template_name = 'dashboard/crud/delete.html'
    success_url = reverse_lazy('dashboard:panel_departamentos')

##### CRUD Num_telefono #####

@method_decorator(login_required, name='dispatch' )
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_verbose_name'] = self.model._meta.verbose_name.title()
        return context

@method_decorator(login_required, name='dispatch' )    
class actualizar_telefono(UpdateView):
    model = Num_telefono
    template_name = 'dashboard/crud/update.html'    
    success_url = reverse_lazy('dashboard:panel_telefonos')
    form_class = TelefonoForm

    def form_valid(self,form):
        numero_tel = form.cleaned_data['numero_tel']
        a = re.search("[0-9]{9}$", numero_tel) #validar telefono
        if not a:
            form.add_error('numero_tel', 'El telefono debe contener 9 caracteres y solo deben ser numericos')
            return self.form_invalid(form)
        return super(actualizar_telefono, self).form_valid(form)

@method_decorator(login_required, name='dispatch' )
class detalle_telefono(DetailView):
    model = Num_telefono
    template_name = 'dashboard/crud/telefono_detail.html'
    success_url = reverse_lazy('dashboard:index')

@method_decorator(login_required, name='dispatch' )
class borrar_telefono(DeleteView):
    model = Num_telefono
    template_name = 'dashboard/crud/delete.html'
    success_url = reverse_lazy('dashboard:panel_telefonos')

### Crud Smartphones ###

@method_decorator(login_required, name='dispatch' )
class crear_smartphone(CreateView):
    model = Smartphones
    template_name = 'dashboard/crud/form.html'
    form_class = SmartphonesForm
    success_url = reverse_lazy('dashboard:panel_smartphones')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_verbose_name'] = self.model._meta.verbose_name.title()
        return context

@method_decorator(login_required, name='dispatch' )    
class actualizar_smartphone(UpdateView):
    model = Smartphones
    template_name = 'dashboard/crud/update.html'    
    success_url = reverse_lazy('dashboard:panel_smartphones')
    form_class = SmartphonesForm

@method_decorator(login_required, name='dispatch' )
class detalle_smartphone(DetailView):
    model = Smartphones
    template_name = 'dashboard/crud/smartphone_detail.html'
    success_url = reverse_lazy('dashboard:panel_smartphones')

@method_decorator(login_required, name='dispatch' )
class borrar_smartphone(DeleteView):
    model = Smartphones
    template_name = 'dashboard/crud/delete.html'
    success_url = reverse_lazy('dashboard:panel_smartphones')

### Crud Tablet ###

@method_decorator(login_required, name='dispatch' )
class crear_tablet(CreateView):
    model = Tablets
    template_name = 'dashboard/crud/form.html'
    form_class = TabletsForm
    success_url = reverse_lazy('dashboard:panel_tablets')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_verbose_name'] = self.model._meta.verbose_name.title()
        return context

@method_decorator(login_required, name='dispatch' )    
class actualizar_tablet(UpdateView):
    model = Tablets
    template_name = 'dashboard/crud/update.html'    
    success_url = reverse_lazy('dashboard:panel_tablets')
    form_class = TabletsForm

@method_decorator(login_required, name='dispatch' )
class detalle_tablet(DetailView):
    model = Tablets
    template_name = 'dashboard/crud/tablet_detail.html'
    success_url = reverse_lazy('dashboard:panel_tablets')

@method_decorator(login_required, name='dispatch' )
class borrar_tablet(DeleteView):
    model = Tablets
    template_name = 'dashboard/crud/delete.html'
    success_url = reverse_lazy('dashboard:panel_tablets')

#### Crud Notebook ###

@method_decorator(login_required, name='dispatch' )
class crear_notebook(CreateView):
    model = Notebooks
    template_name = 'dashboard/crud/form.html'
    form_class = NotebooksForm
    success_url = reverse_lazy('dashboard:panel_notebooks')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_verbose_name'] = self.model._meta.verbose_name.title()
        return context

@method_decorator(login_required, name='dispatch' )    
class actualizar_notebook(UpdateView):
    model = Notebooks
    template_name = 'dashboard/crud/update.html'    
    success_url = reverse_lazy('dashboard:panel_notebooks')
    form_class = NotebooksForm

@method_decorator(login_required, name='dispatch' )
class detalle_notebook(DetailView):
    model = Notebooks
    template_name = 'dashboard/crud/tablet_detail.html'
    success_url = reverse_lazy('dashboard:panel_notebooks')

@method_decorator(login_required, name='dispatch' )
class borrar_notebook(DeleteView):
    model = Notebooks
    template_name = 'dashboard/crud/delete.html'
    success_url = reverse_lazy('dashboard:panel_notebooks')

### Crud Camionetas ###

@method_decorator(login_required, name='dispatch' )
class crear_camioneta(CreateView):
    model = Camionetas
    template_name = 'dashboard/crud/form.html'
    form_class = CamionetasForm
    success_url = reverse_lazy('dashboard:panel_camionetas')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_verbose_name'] = self.model._meta.verbose_name.title()
        return context
    
@method_decorator(login_required, name='dispatch' )    
class actualizar_camioneta(UpdateView):
    model = Camionetas
    template_name = 'dashboard/crud/update.html'    
    success_url = reverse_lazy('dashboard:panel_camionetas')
    form_class = CamionetasForm

@method_decorator(login_required, name='dispatch' )
class detalle_camioneta(DetailView):
    model = Camionetas
    template_name = 'dashboard/crud/tablet_detail.html'
    success_url = reverse_lazy('dashboard:panel_camionetas')

@method_decorator(login_required, name='dispatch' )
class borrar_camioneta(DeleteView):
    model = Camionetas
    template_name = 'dashboard/crud/delete.html'
    success_url = reverse_lazy('dashboard:panel_camionetas')

### Crud asginacion ###

@method_decorator(login_required, name='dispatch' )
class crear_asignacion(CreateView):
    model = Asignacion
    template_name = 'dashboard/crud/form.html'
    form_class = AsignacionForm
    success_url = reverse_lazy('dashboard:panel_asignacion')
### Filtros de Exclusion de equipos asignados y vigentes ###

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        # exclude already assigned smartphones
        #smartphones = form.fields['smartphone_a'].queryset.filter(~Q(asignacion__smartphone_a__isnull=False))
        smartphones = form.fields['smartphone_a'].queryset.filter(
            (Q(asignacion__smartphone_a__isnull=True)
              | Q(asignacion__smartphone_a__isnull=False,
                   asignacion__vigente=False)) 
                & Q(estado_telefono=True)
              )
        form.fields['smartphone_a'].queryset = smartphones

        # Excluir Tablets
        #tablets = form.fields['tablet_a'].queryset.filter(~Q(asignacion__tablet_a__isnull=False))
        tablets = form.fields['tablet_a'].queryset.filter(
            (Q(asignacion__tablet_a__isnull=True)
              | Q(asignacion__tablet_a__isnull=False,
                   asignacion__vigente=False))
                & Q(estado_tablet=True)
        )
        form.fields['tablet_a'].queryset = tablets

        # Excluir Notebooks
        #notebooks = form.fields['notebook_a'].queryset.filter(~Q(asignacion__notebook_a__isnull=False))
        notebooks = form.fields['notebook_a'].queryset.filter(
            (Q(asignacion__notebook_a__isnull=True)
              | Q(asignacion__notebook_a__isnull=False,
                   asignacion__vigente=False))
                & Q(estado_notebook=True)
        )
        form.fields['notebook_a'].queryset = notebooks

        # Excluir Camionetas
        #camioneta = form.fields['camionetas_a'].queryset.filter(~Q(asignacion__camionetas_a__isnull=False))
        camioneta = form.fields['camionetas_a'].queryset.filter(
            (Q(asignacion__camionetas_a__isnull=True)
              | Q(asignacion__camionetas_a__isnull=False,
                   asignacion__vigente=False))
                & Q(disponible=True)
        )
        form.fields['camionetas_a'].queryset = camioneta
        return form

    def form_valid(self, form):
        response = super().form_valid(form)
        return response
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_verbose_name'] = self.model._meta.verbose_name.title()
        return context
        

@method_decorator(login_required, name='dispatch' )    
class actualizar_asignacion(UpdateView):
    model = Asignacion
    template_name = 'dashboard/crud/update.html'    
    success_url = reverse_lazy('dashboard:panel_asignacion')
    form_class = AsignacionForm

@method_decorator(login_required, name='dispatch' )
class detalle_asignacion(DetailView):
    model = Asignacion
    template_name = 'dashboard/crud/tablet_detail.html'
    success_url = reverse_lazy('dashboard:panel_asignacion')

@method_decorator(login_required, name='dispatch' )
class borrar_asignacion(DeleteView):
    model = Asignacion
    template_name = 'dashboard/crud/delete.html'
    success_url = reverse_lazy('dashboard:panel_asignacion')

#### Modelos ####

@method_decorator(login_required, name='dispatch' )
class crear_modelo(CreateView):
    model = Modelos
    template_name = 'dashboard/crud/form.html'
    form_class = ModelosForm
    success_url = reverse_lazy('dashboard:panel_modelos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_verbose_name'] = self.model._meta.verbose_name.title()
        return context

@method_decorator(login_required, name='dispatch' )
class actualizar_modelo(UpdateView):
    model = Modelos
    template_name = 'dashboard/crud/update.html'    
    success_url = reverse_lazy('dashboard:panel_modelos')
    form_class = ModelosForm

@method_decorator(login_required, name='dispatch' )
class detalle_modelo(DetailView):
    model = Modelos
    template_name = 'dashboard/crud/tablet_detail.html'
    success_url = reverse_lazy('dashboard:panel_modelos')

@method_decorator(login_required, name='dispatch' )
class borrar_modelo(DeleteView):
    model = Modelos
    template_name = 'dashboard/crud/delete.html'
    success_url = reverse_lazy('dashboard:panel_modelos')

#### Procesadores ####

@method_decorator(login_required, name='dispatch' )
class crear_procesador(CreateView):
    model = Procesador
    template_name = 'dashboard/crud/form.html'
    form_class = ProcesadorForm
    success_url = reverse_lazy('dashboard:panel_procesadores')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_verbose_name'] = self.model._meta.verbose_name.title()
        return context

@method_decorator(login_required, name='dispatch' )
class actualizar_procesador(UpdateView):
    model = Procesador
    template_name = 'dashboard/crud/update.html'    
    success_url = reverse_lazy('dashboard:panel_procesadores')
    form_class = ProcesadorForm

@method_decorator(login_required, name='dispatch' )
class detalle_procesador(DetailView):
    model = Procesador
    template_name = 'dashboard/crud/tablet_detail.html'
    success_url = reverse_lazy('dashboard:panel_procesadores')

@method_decorator(login_required, name='dispatch' )
class borrar_procesador(DeleteView):
    model = Procesador
    template_name = 'dashboard/crud/delete.html'
    success_url = reverse_lazy('dashboard:panel_procesadores')

#### Marcas ####

@method_decorator(login_required, name='dispatch' )
class crear_marca(CreateView):
    model = Marca
    template_name = 'dashboard/crud/form.html'
    form_class = MarcaForm
    success_url = reverse_lazy('dashboard:panel_marcas')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_verbose_name'] = self.model._meta.verbose_name.title()
        return context

@method_decorator(login_required, name='dispatch' )
class actualizar_marca(UpdateView):
    model = Marca
    template_name = 'dashboard/crud/update.html'    
    success_url = reverse_lazy('dashboard:panel_marcas')
    form_class = MarcaForm

@method_decorator(login_required, name='dispatch' )
class detalle_marca(DetailView):
    model = Marca
    template_name = 'dashboard/crud/tablet_detail.html'
    success_url = reverse_lazy('dashboard:panel_marcas')

@method_decorator(login_required, name='dispatch' )
class borrar_marca(DeleteView):
    model = Marca
    template_name = 'dashboard/crud/delete.html'
    success_url = reverse_lazy('dashboard:panel_marcas')

### Mantenciones ###

@method_decorator(login_required, name='dispatch' )
class crear_mantencion(CreateView):
    model = Mantenciones
    template_name = 'dashboard/crud/form.html'
    form_class = MantencionesForm
    success_url = reverse_lazy('dashboard:panel_mantencion')

@method_decorator(login_required, name='dispatch' )
class actualizar_mantencion(UpdateView):
    model = Mantenciones
    template_name = 'dashboard/crud/update.html'    
    success_url = reverse_lazy('dashboard:panel_mantencion')
    form_class = MantencionesForm

@method_decorator(login_required, name='dispatch' )
class detalle_mantencion(DetailView):
    model = Mantenciones
    template_name = 'dashboard/crud/tablet_detail.html'
    success_url = reverse_lazy('dashboard:panel_mantencion')

@method_decorator(login_required, name='dispatch' )
class borrar_mantencion(DeleteView):
    model = Mantenciones
    template_name = 'dashboard/crud/delete.html'
    success_url = reverse_lazy('dashboard:panel_mantencion')


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
