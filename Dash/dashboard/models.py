#from __future__ import unicode_literals
from enum import auto
from pickle import TRUE
from django.db import models
from django.forms import NullBooleanField
from django.utils import timezone

class Departamentos(models.Model):
    id = models.IntegerField(null=False,blank=False,unique=True,primary_key=True)
    area = models.CharField(max_length=20,null=False)
    sucursal = models.CharField(max_length=20,null=False)

class Num_telefono(models.Model):
    id = models.IntegerField(null=False,blank=False,unique=True)
    numero_tel = models.CharField(max_length=10,null=False,blank=False,unique=True)
    activo = models.BooleanField(default=False) #numero activo o dado de baja

class Series(models.Model):
    id = models.IntegerField(null=False,blank=False,unique=True,primary_key=True)
    serie = models.CharField(max_length=20,null=False,blank=False,unique=True)
    fecha_compra = models.DateTimeField(default=timezone.now) #Establece la fecha local
    valor = models.IntegerField(blank=True)
    imei_1 = models.IntegerField(max_length=20,blank=True,null=True)
    imei_2 = models.IntegerField(max_length=20,blank=True,null=True)

class  Usuarios(models.Model):
    rut = models.CharField(max_length=10, null=False, blank=False, unique=True,primary_key=True)
    nombre = models.CharField(max_length=20, null=False)
    apellido = models.CharField(max_length=20, null=False)
    area = models.ForeignKey(Departamentos,to_field='area') #revisar
    correo = models.CharField(max_length=50)
    Telefono = models.ForeignKey(Num_telefono,to_field='numero_tel',on_delete=models.SET_NULL) #revisar

class Equipos(models.Model):
    id = models.IntegerField(unique=True, null=False,blank=False,primary_key=True)
    usuario = models.ForeignKey(Usuarios,on_delete=models.SET_NULL)
    tipo = models.CharField(max_length=10,null=False)
    modelo = models.CharField(max_length=20,null=False)
    serie = models.ForeignKey(Series,to_field='serie')
    operativo = models.BooleanField(default=True, null=False)
    nuevo = models.NullBooleanField(default=True,null=False) #Nuevo / Usado
    observaciones = models.CharField(max_length=50) #pantalla rota, con mica, etc.

class historial(models.Model):
    id = models.IntegerField(unique=True,null=False,blank=False,primary_key=True)
    usuario = models.ForeignKey(Usuarios)
    equipo = models.ForeignKey(Equipos)
    fecha_recepcion = models.DateTimeField(default=timezone.now)
    fecha_entrega = models.DateTimeField(auto_now_add=True)

# Create your models here.
