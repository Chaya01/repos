#from django.conf.urls import url
from django.urls import path
#from . import views
from dashboard import views
from django.urls import re_path
from .views import *

app_name = 'dashboard'

urlpatterns = [
    #path('', views.index, name='index'),
    #path('',views.inicio,name='inicio',),

    ### Inicio ###
    path('', index.as_view(), name='index'),

    ### Usuarios ###
    path('usuario/<str:pk>', detalle_usuario.as_view(), name='userdetail'),
    path('usuario/form/', crear_usuario.as_view(), name='newuser'),
    path('usuario/update/<str:pk>', actualizar_usuario.as_view(), name='edituser'),
    path('usuario/delete/<str:pk>', borrar_usuario.as_view(), name='deleteuser'),

    ### Departamentos ###
    path('departamento/<str:pk>', detalle_departamento.as_view(), name='depadetail'),
    path('departamento/form/', crear_departamento.as_view(),name='newdepa'),
    path('departamento/update/<str:pk>', actualizar_departamento.as_view(), name='editdepa'),
    path('departamento/delete/<str:pk>', borrar_departamento.as_view(), name= 'deletedepa'),

    ### Telefonos ###
    path('telefonos/<str:pk>', detalle_telefono.as_view(), name ='teldetail'),
    path('telefonos/form/', crear_telefono.as_view(), name = 'newtel'),
    path('telefonos/update/<str:pk>', actualizar_telefono.as_view(), name= 'edittel'),
    path('telefonos/delete/<str:pk>', borrar_telefono.as_view(), name = 'deletetel'),

    ### Series ###
    path('series/<str:pk>', detalle_serie.as_view(), name='seriedetail'),
    path('series/form/', crear_serie.as_view(), name='newserie'),
    path('series/update/<str:pk>', actualizar_serie.as_view(), name= 'editserie'),
    path('series/delete/<str:pk>', borrar_serie.as_view(), name= 'deleteserie'),


]