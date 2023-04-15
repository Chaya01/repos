#from django.conf.urls import url
from django.urls import path
#from . import views
from dashboard import views
from django.urls import re_path
from .views import *
from django.urls import include, path


app_name = 'dashboard'

urlpatterns = [
    #path('', views.index, name='index'),
    #path('',views.inicio,name='inicio',),

    ### Inicio ###
    path('', views.login_request, name="login"),

    path('index.html', index.as_view(), name='index'),



    #Paneles#

    path('panel_usuarios.html',panel_usuarios.as_view(),name ='panel_usuarios'),
    path('panel_telefonos.html',panel_telefonos.as_view(),name ='panel_telefonos'),
    path('panel_smartphones.html',panel_smartphones.as_view(),name ='panel_smartphones'),
    path('panel_tablets.html',panel_tablets.as_view(),name ='panel_tablets'),
    path('panel_notebooks.html',panel_notebooks.as_view(),name ='panel_notebooks'),
    path('panel_camionetas.html',panel_camionetas.as_view(),name ='panel_camionetas'),
    path('panel_asginacion.html',panel_asignacion.as_view(),name ='panel_asignacion'),
    path('panel_modelos.html',panel_modelos.as_view(),name ='panel_modelos'),
    path('panel_procesadores.html',panel_procesadores.as_view(),name ='panel_procesadores'),
    path('panel_marcas.html',panel_marcas.as_view(),name ='panel_marcas'),
    path('panel_mantencion.html',panel_mantenciones.as_view(),name ='panel_mantencion'),
    path('mantencion/<int:pk>', views.listado_mantenciones.as_view(), name = 'mantenciones'),
    path('usuarios/<int:pk>', views.reporte.as_view(), name = 'reporte'),
    path('reporte/<int:pk>/imprimir/', imprimir_reporte, name='imprimir_reporte'),




    ### Usuarios ###
    path('usuario/<str:pk>', detalle_usuario.as_view(), name='userdetail'),
    path('usuario/form/', crear_usuario.as_view(), name='newuser'),
    path('usuario/update/<str:pk>', actualizar_usuario.as_view(), name='edituser'),
    path('usuario/delete/<str:pk>', borrar_usuario.as_view(), name='deleteuser'),
    path('usuarios/<int:pk>/imprimir_reporte/', imprimir_reporte, name='imprimir_reporte'),


    ### Telefonos ###
    path('telefonos/<str:pk>', detalle_telefono.as_view(), name ='teldetail'),
    path('telefonos/form/', crear_telefono.as_view(), name = 'newtel'),
    path('telefonos/update/<str:pk>', actualizar_telefono.as_view(), name= 'edittel'),
    path('telefonos/delete/<str:pk>', borrar_telefono.as_view(), name = 'deletetel'),

    ### Smartphones ###
    path('smartphones/<str:pk>', detalle_smartphone.as_view(), name ='smadetail'),
    path('smartphones/form/', crear_smartphone.as_view(), name = 'newsma'),
    path('smartphones/update/<str:pk>', actualizar_smartphone.as_view(), name= 'editsma'),
    path('smartphones/delete/<str:pk>', borrar_smartphone.as_view(), name = 'deletsma'),

    ### Tablets ###
    path('tablets/<str:pk>', detalle_tablet.as_view(), name ='tadetail'),
    path('tablets/form/', crear_tablet.as_view(), name = 'newta'),
    path('tablets/update/<str:pk>', actualizar_tablet.as_view(), name= 'edita'),
    path('tablets/delete/<str:pk>', borrar_tablet.as_view(), name = 'deleta'),

    ### Notebooks ###
    path('notebooks/<str:pk>', detalle_notebook.as_view(), name ='notdetail'),
    path('notebooks/form/', crear_notebook.as_view(), name = 'newnot'),
    path('notebooks/update/<str:pk>', actualizar_notebook.as_view(), name= 'editnot'),
    path('notebooks/delete/<str:pk>', borrar_notebook.as_view(), name = 'deletnot'),

    ### Camionetas ###
    path('camionetas/<str:pk>', detalle_camioneta.as_view(), name ='camdetail'),
    path('camionetas/form/', crear_camioneta.as_view(), name = 'newcam'),
    path('camionetas/update/<str:pk>', actualizar_camioneta.as_view(), name= 'editcam'),
    path('camionetas/delete/<str:pk>', borrar_camioneta.as_view(), name = 'deletcam'),

    ### Asignaciones ###
    path('asignacion/<str:pk>', detalle_asignacion.as_view(), name ='asgdetail'),
    path('asignacion/form/', crear_asignacion.as_view(), name = 'newasg'),
    path('asignacion/update/<str:pk>', actualizar_asignacion.as_view(), name= 'editasg'),
    path('asignacion/delete/<str:pk>', borrar_asignacion.as_view(), name = 'deletasg'),

        ### Modelos ###
    path('modelos/<str:pk>', detalle_modelo.as_view(), name ='moddetail'),
    path('modelos/form/', crear_modelo.as_view(), name = 'newmod'),
    path('modelos/update/<str:pk>', actualizar_modelo.as_view(), name= 'editmod'),
    path('modelos/delete/<str:pk>', borrar_modelo.as_view(), name = 'deletmod'),

        ### Procesador ###
    path('procesador/<str:pk>', detalle_procesador.as_view(), name ='prodetail'),
    path('procesador/form/', crear_procesador.as_view(), name = 'newpro'),
    path('procesador/update/<str:pk>', actualizar_procesador.as_view(), name= 'editpro'),
    path('procesador/delete/<str:pk>', borrar_procesador.as_view(), name = 'deletpro'),

        ### Marcas ###
    path('marcas/<str:pk>', detalle_marca.as_view(), name ='madetail'),
    path('marcas/form/', crear_marca.as_view(), name = 'newma'),
    path('marcas/update/<str:pk>', actualizar_marca.as_view(), name= 'editma'),
    path('marcas/delete/<str:pk>', borrar_marca.as_view(), name = 'deletma'),

        ### Mantenciones ###
    path('mantencion/<str:pk>', detalle_mantencion.as_view(), name ='mantedetail'),
    path('mantencion/form/', crear_mantencion.as_view(), name = 'newmante'),
    path('mantencion/update/<str:pk>', actualizar_mantencion.as_view(), name= 'editmante'),
    path('mantencion/delete/<str:pk>', borrar_mantencion.as_view(), name = 'deletmante'),

    path('cargar_excel/', cargar_excel, name='cargar_excel'),
    ### Series ###
#    path('series/<str:pk>', detalle_serie.as_view(), name='seriedetail'),
#    path('series/form/', crear_serie.as_view(), name='newserie'),
#    path('series/update/<str:pk>', actualizar_serie.as_view(), name= 'editserie'),
#    path('series/delete/<str:pk>', borrar_serie.as_view(), name= 'deleteserie'),


]