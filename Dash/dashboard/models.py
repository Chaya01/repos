#from __future__ import unicode_literals
from contextlib import nullcontext
from enum import auto
from pickle import FALSE, TRUE
from tkinter import CASCADE
from django.db import models
from django.forms import NullBooleanField
from django.utils import timezone

class Departamentos(models.Model):
    area = models.CharField(max_length=20,null=True)
    sucursal = models.CharField(max_length=20,null=False)

    def nombre_departamento(self):
        return u"{} {}".format(
            self.area,
            self.sucursal
        )
    def __str__(self):
        return self.area

class Num_telefono(models.Model):
    numero_tel = models.CharField(max_length=9,null=True,blank=True)
    activo = models.BooleanField(default=False) #numero activo o dado de baja

    def __str__(self):
        return self.numero_tel

    def numero_telefonico(self):
        return self.numero_tel
    
    def numero_activo(self):
        return self.activo

#Forma larga y poco eficiente de respaldo#    
'''class Marcas_smartphones(models.Models):
    marcas_sm = models.CharField(max_length=20,primary_key=True)

    def __str__(self):
        return self.marcas_sm

class Modelos_smartphones(models.Models):
    marca_sm = models.ForeignKey(Marcas_smartphones,on_delete=models.SET_NULL)
    modelo_sm = models.CharField(max_length=20)

    def __str__(self):
        return self.modelo_sm
    
class Marcas_tablets(models.Models):
    marcas_tb = models.CharField(max_length=20,primary_key=True)

    def __str__(self):
        return self.marcas_tb

class Modelos_tablets(models.Models):
    marca_tb = models.ForeignKey(Marcas_tablets,on_delete=models.SET_NULL)
    modelo_tb = models.CharField(max_length=20)

    def __str__(self):
        return self.modelo_tb

class Marcas_notebook(models.Models):
    marcas_nt = models.CharField(max_length=20,primary_key=True)

    def __str__(self):
        return self.marcas_nt

class Modelos_notebook(models.Models):
    marca_nt = models.ForeignKey(Marcas_notebook,on_delete=models.SET_NULL)
    modelo_nt = models.CharField(max_length=20)

    def __str__(self):
        return self.modelo_nt

class Marcas_camionetas(models.Models):
    marcas_cm = models.CharField(max_length=20,primary_key=True)

    def __str__(self):
        return self.marcas_cm

class Modelos_camionetas(models.Models):
    marca_cm = models.ForeignKey(Marcas_camionetas,on_delete=models.SET_NULL)
    modelo_cm = models.CharField(max_length=20)

    def __str__(self):
        return self.modelo_cm
'''

#Prueba de parametrizacion#

class Marca(models.Model):
    marca = models.CharField(max_length=20, unique= True)

    def __str__(self):
        return self.marca

class ParamTipo(models.Model):
    nombre_param = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.nombre_param

class Modelos(models.Model):
    m_marca = models.ForeignKey(Marca,on_delete=models.CASCADE)
    m_param = models.ForeignKey(ParamTipo,on_delete=models.CASCADE)
    m_modelo = models.CharField(max_length=20,unique=True)

    def __str__(self):
        return str(u"{} {} {}").format(
            self.m_marca,
            self.m_modelo,
            self.m_param,
        )

####
class Smartphones(models.Model):
    serie_smartphone = models.CharField(unique=True,max_length=20)
    modelo_smartphone = models.ForeignKey(Modelos,on_delete=models.CASCADE)
    imei1 = models.IntegerField(unique=True,)
    imei2 = models.IntegerField(unique = True, null=True)
    estado_telefono = models.BooleanField(default=True,) #Nuevo / Usado
    fecha_compra_telefono = models.DateField(help_text='Fecha en la que se recepciona el equipo en la empresa')
    valor_telefono = models.IntegerField(help_text='Por favor inserte el valor en CLP')
    funciona_telefono = models.BooleanField(default=True, null=False) #si / no
    observaciones_telefonos = models.CharField(max_length=50,blank=True) #pantalla rota, con mica, etc.

    def __str__(self):
        return str(u"{} {}").format(
            self.modelo_smartphone,
            self.serie_smartphone,
        )
    
class Tablets(models.Model): #crear views, forms and urls
    serie_tablet = models.CharField(unique=True,max_length=20)
    modelo_tablet = models.ForeignKey(Modelos,on_delete=models.CASCADE)
    imei_tb = models.CharField (max_length=20,null=True, unique=True)
    fecha_compra_tablet = models.DateField(help_text='Fecha en la que se recepciona el equipo en la empresa')
    valor_tablet = models.IntegerField(help_text='Por favor inserte el valor en CLP')
    observaciones_tablets = models.CharField(max_length=50,blank=True)

    def __str__(self):
        return str(u"{} {}").format(
            self.modelo_tablet,
            self.serie_tablet,
        )
    
class Notebooks(models.Model):
    serie_notebook = models.CharField(unique=True,max_length=20)
    modelo_notebook = models.ForeignKey(Modelos,on_delete=models.CASCADE)
    fecha_compra_notebook = models.DateField(help_text='Fecha en la que se recepciona el equipo en la empresa')
    valor_notebook = models.IntegerField(help_text='Por favor inserte el valor en CLP')
    observaciones_notebook = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return str (u"{}").format(
            self.modelo_notebook,
        )
    
class Camionetas(models.Model):
    patente = models.CharField(max_length=20,unique=True)
    modelo_camioneta = models.ForeignKey(Modelos,on_delete=models.CASCADE)
    mantencion = models.DateField()
    observaciones_camionetas = models.CharField(max_length=50)

    def __str__(self):
        return u"{} {}".format(
            self.patente,
            self.modelo_camioneta,
        )

class  Usuarios(models.Model): #Editar Views and Forms.
    rut = models.CharField(max_length=10, null=False, blank=False, unique=True)
    nombre = models.CharField(max_length=20, null=False)
    apellido = models.CharField(max_length=20, null=False)
    area = models.ForeignKey(Departamentos,on_delete=models.SET_NULL, null=True) #revisar
    correo = models.EmailField(max_length=50)

#    def nombre_completo(self):
#        return u"{} {}".format(
#            self.nombre,
#            self.apellido
#        )
    def __str__(self):
        return u"{} {}".format(
            self.nombre,
            self.apellido
        )
    
#Datos Redundantes por la tabla Asignacion #
''' numero_asignado = models.ForeignKey(Num_telefono,on_delete=models.SET_NULL, null=True) #revisar
    telefono_asignado = models.ForeignKey(Smartphones, on_delete= models.CASCADE) 
    tablet_asignada = models.ForeignKey(Tablets, on_delete= models.CASCADE)
    notebook_asignado = models.ForeignKey(Notebooks,on_delete= models.CASCADE)
    camioneta_asignada = models.ForeignKey(Camionetas, on_delete= models.CASCADE)
''' 
#Datos Redundantes por la tabla Asignacion #


class Asignacion(models.Model):
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    num = models.ForeignKey(Num_telefono, on_delete=models.CASCADE,null=True,blank=True)
    smartphone_a = models.ForeignKey(Smartphones, on_delete=models.CASCADE)
    tablet_a = models.ForeignKey(Tablets, on_delete=models.CASCADE)
    notebook_a = models.ForeignKey(Notebooks, on_delete=models.CASCADE)
    camionetas_a =models.ForeignKey(Camionetas, on_delete=models.CASCADE)
    vigente = models.BooleanField(help_text='marcar si es la asignacion actual del usuario.') #registro actual, si / no)


# Sin uso, modelo anterior


#class Series(models.Model):
#    id = models.AutoField(null=False,blank=False,unique=True,primary_key=True)
#    serie = models.CharField(max_length=20,null=False,blank=False,unique=True)
#    fecha_compra = models.DateTimeField(default=timezone.now) #Establece la fecha local
#    valor = models.IntegerField(blank=True)
#    imei_1 = models.IntegerField(blank=True,null=True)
#    imei_2 = models.IntegerField(blank=True,null=True)

#    def __str__(self):
#        return self.serie

#    def imprimir_serie(self):
#        return self.serie

 #   def imprimir_fecha_compra(self):
 #       return self.fecha_compra

  #  def imprimir_valor(self):
  #      return self.valor

    #crear return de imei

    #class Historial(models.Model):
#    id = models.AutoField(unique=True,null=False,blank=False,primary_key=True)
#    usuario = models.ForeignKey(Usuarios,on_delete=models.PROTECT)
#    equipo = models.ForeignKey(Equipos,on_delete=models.PROTECT)
#    fecha_recepcion = models.DateTimeField(default=timezone.now)
#    fecha_entrega = models.DateTimeField(auto_now_add=True)#(default=timezone.now)
#
#    def __str__(self):
 #       return str(self.usuario)

    #def registro(self):
    #    return u"{} {} {} {}".format(
    #        self.usuario,
    #        self.equipo,
    #        self.fecha_recepcion,
    #        self.fecha_entrega
    #    )

