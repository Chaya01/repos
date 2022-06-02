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
    path('', index.as_view(), name='index'),
    path('usuario/<str:pk>', detalle_usuario.as_view(), name='userdetail'),
    path('usuario/form/', crear_usuario.as_view(), name='newuser'),
    path('usuario/update/<str:pk>', actualizar_usuario.as_view(), name='edituser'),
    path('usuario/delete/<str:pk>', borrar_usuario.as_view(), name='deleteuser'),
    path('departamento/<str:pk>', detalle_departamento.as_view(), name='depadetail'),
    path('departamento/form/', crear_departamento.as_view(),name='newdepa'),


]