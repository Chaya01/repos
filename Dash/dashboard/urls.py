#from django.conf.urls import url
from django.urls import path
#from . import views
from dashboard import views

app_name = 'Inventario'

urlpatterns = [
    #path('', views.index, name='index'),

    path(
        '',
        views.Usuarios,
        name='Usuarios',
    )
]