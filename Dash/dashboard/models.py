#from __future__ import unicode_literals
from enum import auto
from pickle import TRUE
from tkinter import CASCADE
from django.db import models
from django.forms import NullBooleanField
from django.utils import timezone

class Departamentos(models.Model):
    id = models.IntegerField(null=False,blank=False,unique=True,primary_key=True)
    area = models.CharField(max_length=20,null=False)
    sucursal = models.CharField(max_length=20,null=False)

    def nombre_departamento(self):
        return u"{} {}".format(
            self.area,
            self.sucursal
        )

class Num_telefono(models.Model):
    id = models.IntegerField(null=False,blank=False,unique=True,primary_key=True)
    numero_tel = models.CharField(max_length=10,null=False,blank=False,unique=True)
    activo = models.BooleanField(default=False) #numero activo o dado de baja

    def numero_telefonico(self):
        return self.numero_tel
    
    def numero_activo(self):
        return self.activo

class Series(models.Model):
    id = models.IntegerField(null=False,blank=False,unique=True,primary_key=True)
    serie = models.CharField(max_length=20,null=False,blank=False,unique=True)
    fecha_compra = models.DateTimeField(default=timezone.now) #Establece la fecha local
    valor = models.IntegerField(blank=True)
    imei_1 = models.IntegerField(blank=True,null=True)
    imei_2 = models.IntegerField(blank=True,null=True)

    def imprimir_serie(self):
        return self.serie

    def imprimir_fecha_compra(self):
        return self.fecha_compra

    def imprimir_valor(self):
        return self.valor

    #crear return de imei

class  Usuarios(models.Model):
    rut = models.CharField(max_length=10, null=False, blank=False, unique=True,primary_key=True)
    nombre = models.CharField(max_length=20, null=False)
    apellido = models.CharField(max_length=20, null=False)
    area = models.ForeignKey(Departamentos,on_delete=models.CASCADE) #revisar
    correo = models.CharField(max_length=50)
    Telefono = models.ForeignKey(Num_telefono,on_delete=models.CASCADE) #revisar

    def nombre_completo(self):
        return u"{} {}".format(
            self.nombre,
            self.apellido
        )

class Equipos(models.Model):
    id = models.IntegerField(unique=True, null=False,blank=False,primary_key=True)
    usuario = models.ForeignKey(Usuarios,on_delete=models.CASCADE)
    tipo = models.CharField(max_length=10,null=False)
    modelo = models.CharField(max_length=20,null=False)
    serie = models.ForeignKey(Series,on_delete=models.CASCADE)
    operativo = models.BooleanField(default=True, null=False)
    nuevo = models.BooleanField(default=True,null=False) #Nuevo / Usado
    observaciones = models.CharField(max_length=50) #pantalla rota, con mica, etc.

    def asignacion(self):
        return u"{} {} {} {}".format(
            self.usuario,
            self.tipo,
            self.modelo,
            self.serie
        )

class Historial(models.Model):
    id = models.IntegerField(unique=True,null=False,blank=False,primary_key=True)
    usuario = models.ForeignKey(Usuarios,on_delete=models.CASCADE)
    equipo = models.ForeignKey(Equipos,on_delete=models.CASCADE)
    fecha_recepcion = models.DateTimeField(default=timezone.now)
    fecha_entrega = models.DateTimeField(default=timezone.now)#auto_now_add=True)

    def registro(self):
        return u"{} {} {} {}".format(
            self.usuario,
            self.equipo,
            self.fecha_recepcion,
            self.fecha_entrega
        )

# Create your models here.
