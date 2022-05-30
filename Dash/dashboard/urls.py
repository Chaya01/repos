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
    path('', listado.as_view(), name='list'),
    path('usuario/<str:pk>', detalle_usuario.as_view(), name='detail'),
    path('usuario/nuevo', detalle_usuario.as_view(), name='new'),
    path('usuario/<str:pk>', detalle_usuario.as_view(), name='edit'),
    path('usuario/<str:pk>', detalle_usuario.as_view(), name='delete'),

]