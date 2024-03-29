#from __future__ import unicode_literals
from django.db import models
from django.utils.translation import gettext as _
from .listados import *

class Procesador(models.Model):
    marca_procesador = models.CharField(choices=listado_procesadores,max_length=20,verbose_name='Marca Procesador')
    modelo_p = models.CharField(max_length=20,verbose_name='Modelo')
    ghz = models.DecimalField(max_digits=2,decimal_places=1,verbose_name='Ghz')
    nucleos = models.IntegerField(verbose_name='Cores')
    año_mf = models.IntegerField(verbose_name='Año manufactura')

    def __str__ (self):
        return str(u"{} - {}").format(
            self.marca_procesador,
            self.modelo_p,
        )
    class Meta: 
        ordering = ['marca_procesador']

class Estados(models.Model):
    e_equipos = models.BooleanField(default=False)

    def __str__ (self):
        return str(self.e_equipos)


#    def __str__(self):          #nombre Visible#
#        return self.area

class Num_telefono(models.Model):    
    numero_tel = models.CharField(max_length=9,null=True,blank=True,unique=True,verbose_name="Numero")
    activo = models.BooleanField(verbose_name="contratado") #numero activo o dado de baja

    def __str__(self):
        return self.numero_tel

    def numero_telefonico(self):
        return self.numero_tel
    
    def numero_activo(self):
        return self.activo
    
    class Meta:
        verbose_name = "Telefono"
    
#Prueba de parametrizacion#

class Marca(models.Model):
    marca = models.CharField(max_length=20, unique= True)

    def __str__(self):
        return self.marca

class ParamTipo(models.Model):
    nombre_param = models.CharField(max_length=20, unique=True) #camioneta,tablet,notebook,smartphone

    def __str__(self):
        return self.nombre_param

class Modelos(models.Model):
    
    m_marca = models.ForeignKey(Marca,on_delete=models.CASCADE,verbose_name='Marca')
    m_param = models.ForeignKey(ParamTipo,on_delete=models.CASCADE,verbose_name='Tipo')
    m_modelo = models.CharField(max_length=50,unique=True,verbose_name='Modelo')
    m_procesador = models.ForeignKey(Procesador,default="01",on_delete=models.SET_DEFAULT,help_text="Por favor marcar 'No aplica' para las camionetas"
                                     ,verbose_name='Procesador')

    def __str__(self):
        return str(u"{} - {}").format(
            self.m_marca,
            self.m_modelo,  
        )
    class Meta: 
        ordering = ['m_marca']

####
class Smartphones(models.Model):
    serie_smartphone = models.CharField(unique=True,max_length=25)
    modelo_smartphone = models.ForeignKey(Modelos,on_delete=models.CASCADE)
    imei1 = models.CharField(max_length=20,unique=True,)
    imei2 = models.CharField(max_length=20,unique = True, null=True,blank=True)
    estado_telefono = models.BooleanField()
    fecha_compra_telefono = models.DateField(help_text='Fecha en la que se recepciona el equipo en la empresa')
    valor_telefono = models.IntegerField(help_text='Por favor inserte el valor en CLP')
#    funciona_telefono = models.ForeignKey(default=True, null=False) #si / no
    observaciones_telefonos = models.CharField(max_length=100,blank=True) #pantalla rota, con mica, etc.
    sram = models.IntegerField(verbose_name='Memoria Ram')

    def __str__(self):
        return str(u"{} {}").format(
            self.modelo_smartphone,
            self.serie_smartphone,
        )
    class Meta: 
        ordering = ['modelo_smartphone']
    
class Tablets(models.Model): #crear views, forms and urls
    serie_tablet = models.CharField(unique=True,max_length=25)
    modelo_tablet = models.ForeignKey(Modelos,on_delete=models.CASCADE)
    imei_tb = models.CharField (max_length=20,null=True,blank=True)
    estado_tablet = models.BooleanField()   
    fecha_compra_tablet = models.DateField(help_text='Fecha en la que se recepciona el equipo en la empresa')
    valor_tablet = models.IntegerField(help_text='Por favor inserte el valor en CLP')
    observaciones_tablets = models.CharField(max_length=100,blank=True)
    tram = models.IntegerField(verbose_name='Memoria Ram')

    def __str__(self):
        return str(u"{} {}").format(
            self.modelo_tablet,
            self.serie_tablet,
        )
    class Meta: 
        ordering = ['modelo_tablet']
    
class Notebooks(models.Model):
    serie_notebook = models.CharField(unique=True,max_length=25)
    modelo_notebook = models.ForeignKey(Modelos,on_delete=models.CASCADE)
    estado_notebook = models.BooleanField()
    fecha_compra_notebook = models.DateField(help_text='Fecha en la que se recepciona el equipo en la empresa')
    mantencion_notebook = models.DateField(help_text="Fecha de la ultima mantecion")
    valor_notebook = models.IntegerField(help_text='Por favor inserte el valor en CLP')
    observaciones_notebook = models.CharField(max_length=100, blank=True)
    nram = models.IntegerField(verbose_name='Memoria Ram')
    nhdd = models.IntegerField(verbose_name='HDD',help_text='Por favor marcar 0 si no tiene HDD')
    nssd = models.IntegerField(verbose_name='SSD',help_text='Por favor marcar 0 si no tiene SSD')

    def __str__(self):
        return str (u"{} - {}").format(
            self.modelo_notebook,
            self.serie_notebook,
        )
    class Meta: 
        ordering = ['modelo_notebook']
    
class Camionetas(models.Model):
    patente = models.CharField(max_length=20,unique=True)
    modelo_camioneta = models.ForeignKey(Modelos,on_delete=models.CASCADE)
    mantencion = models.DateField()
    observaciones_camionetas = models.CharField(max_length=100)
    disponible = models.BooleanField()
    modalidad = models.CharField(choices=listado_modalidades,max_length=20,verbose_name='listado modalidades')
    vin = models.CharField(max_length=20,unique=True)
    kilometraje = models.IntegerField()
    fecha_recepcion = models.DateField(null=True,blank=True)
    fecha_entrega = models.DateField(null=True,blank=True)

    def __str__(self):
        return (u"{} {}").format(
            self.patente,
            self.modelo_camioneta,
        )
    class Meta: 
        ordering = ['patente']

class  Usuarios(models.Model): #Editar Views and Forms.
    rut = models.CharField(max_length=10, null=False, blank=False, unique=True)
    nombre = models.CharField(max_length=30, null=False)
    apellido = models.CharField(max_length=20, null=False)
    correo = models.EmailField(max_length=50,null=True, blank=True)
    empresa = models.CharField(max_length=20)
    gerente = models.CharField(max_length=20)
    centro_de_costo = models.CharField(choices=listado_centrosdecostos, max_length=30, verbose_name='Centro de Costo')

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
    
    class Meta:
        verbose_name = "Trabajadores" 
        ordering = ['nombre']
    
#Datos Redundantes por la tabla Asignacion #
''' numero_asignado = models.ForeignKey(Num_telefono,on_delete=models.SET_NULL, null=True) #revisar
    telefono_asignado = models.ForeignKey(Smartphones, on_delete= models.CASCADE) 
    tablet_asignada = models.ForeignKey(Tablets, on_delete= models.CASCADE)
    notebook_asignado = models.ForeignKey(Notebooks,on_delete= models.CASCADE)
    camioneta_asignada = models.ForeignKey(Camionetas, on_delete= models.CASCADE)
''' 
#Datos Redundantes por la tabla Asignacion #


class Asignacion(models.Model):
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE,verbose_name="Trabajador")
    num = models.ForeignKey(Num_telefono, on_delete=models.CASCADE,null=True,blank=True,verbose_name="Numero de telefono")
    smartphone_a = models.ForeignKey(Smartphones, on_delete=models.CASCADE, null=True,blank=True,verbose_name="Smartphone")
    fecha_sma = models.DateField(default= None,null=True,blank=True,verbose_name="Fecha de entrega")
    tablet_a = models.ForeignKey(Tablets, on_delete=models.CASCADE,null=True,blank=True,verbose_name="Tablet")
    fecha_ta = models.DateField(default= None,null=True,blank=True,verbose_name="Fecha de entrega")
    notebook_a = models.ForeignKey(Notebooks, on_delete=models.CASCADE,null=True,blank=True,verbose_name="Notebook")
    fecha_nt = models.DateField(default= None,null=True,blank=True,verbose_name="Fecha de entrega")
    camionetas_a =models.ForeignKey(Camionetas, on_delete=models.CASCADE,null=True,blank=True,verbose_name="Camioneta")
    fecha_cm = models.DateField(default= None,null=True,blank=True,verbose_name="Feha de entrega")
    vigente = models.BooleanField(help_text='marcar si es la asignacion actual del usuario.') #registro actual, si / no)

    def __str__(self):
        return str(self.usuario)
    
class Mantenciones(models.Model):
    m_patente = models.ForeignKey(Camionetas, on_delete=models.CASCADE)
    fecha_mantencion = models.DateField(default= None)
    m_kilometraje = models.IntegerField(verbose_name='Kilometraje aproximado de la mantencion')
    m_estado = models.BooleanField(default=False)
    responsable = models.ForeignKey(Asignacion,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.m_patente)