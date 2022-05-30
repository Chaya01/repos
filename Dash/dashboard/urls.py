#from django.conf.urls import url
from django.urls import path
#from . import views
from dashboard import views
from django.urls import re_path
from .views import (
    listado,
    detalle_usuario,
    crear_usuario,
    actualizar_usuario,
    borrar_usuario
)

app_name = 'dashboard'

urlpatterns = [
    #path('', views.index, name='index'),
    #path('',views.inicio,name='inicio',),
    re_path(r'^$', listado.as_view(), name='listado'),
    re_path(r'^(?P<pk>\d+)$', detalle_usuario.as_view(), name='detalle'),
    re_path(r'^nuevo$', crear_usuario.as_view(), name='crear'),
    re_path(r'^editar/(?P<pk>\d+)$',actualizar_usuario.as_view(), name='actualizar'),
    re_path(r'^eliminar/(?P<pk>\d+)$', borrar_usuario.as_view(), name='eliminar'),
]