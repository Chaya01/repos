from django import forms
from .models import *
import re
from django.core.exceptions import ValidationError
from django.db.models import Q
from .listados import *


class EstadosForm(forms.ModelForm):
    class Meta:
        model = Estados
        fields = ['e_equipos']

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = ['rut', 'nombre','apellido','area', 'correo','empresa','gerente','centro_de_costo']

        widgets ={
            'empresa' : forms.Select(choices=listado_empresas,attrs={'class':'form-control'}),
            'gerente' : forms.Select(choices=listado_gerentes,attrs={'class':'form-control'}),
            'centro_de_costo' : forms.Select(choices=listado_centrosdecostos,attrs={'class':'form-control'}),

        }

class DepartamentoForm(forms.ModelForm):
    class Meta:
        model = Departamentos
        fields = ['area','sucursal']

        widgets ={
            'area' : forms.Select(choices=listado_areas,attrs={'class':'form-control'}),
            'sucursal' : forms.Select(choices=listado_sucursales,attrs={'class':'form-control'}),
        }

class TelefonoForm(forms.ModelForm):
    class Meta:
        model = Num_telefono
        fields = ['numero_tel','activo']

class SmartphonesForm(forms.ModelForm):

    ######filtro por tipo ##### 01 Smartphone ###
    def __init__(self,*args,**kwargs): 
            super (SmartphonesForm,self ).__init__(*args,**kwargs)
            self.fields['modelo_smartphone'].queryset = Modelos.objects.filter(m_param='01')

    class Meta:
        model = Smartphones
        fields = ['serie_smartphone','modelo_smartphone',
                  'imei1','imei2','estado_telefono','fecha_compra_telefono',
                  'valor_telefono','observaciones_telefonos','sram']
        
        widgets = {
            'fecha_compra_telefono' : forms.DateInput(
            format="%d/%m/%Y",attrs={'type':'date',
                                     'class': 'dtpicker',
                                     'required':"true",
                                     }
            )
        }

class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = ['marca']

class ParamTipoForm(forms.ModelForm):
    class Meta:
        model = ParamTipo
        fields = ['nombre_param']

class ModelosForm(forms.ModelForm):
    class Meta:
        model = Modelos
        fields = ['m_marca','m_param','m_modelo','m_procesador']

class TabletsForm(forms.ModelForm):

    def __init__(self,*args,**kwargs): ### Filtro de tipo ### 02 Tablet
            super (TabletsForm,self ).__init__(*args,**kwargs)
            self.fields['modelo_tablet'].queryset = Modelos.objects.filter(m_param='02')

    class Meta:
        model = Tablets
        fields = ['serie_tablet','modelo_tablet','imei_tb','estado_tablet','fecha_compra_tablet',
                  'valor_tablet','observaciones_tablets','tram']
        
        widgets = {
            'fecha_compra_tablet' : forms.DateTimeInput(
            format="%d/%m/%Y",attrs={'type':'date','class': 'dtpicker',
                                     'required':"true"}
            )
        }        

class NotebooksForm(forms.ModelForm):

    def __init__(self,*args,**kwargs): ### Filtro de tipo ### 03 Notebook
            super (NotebooksForm,self ).__init__(*args,**kwargs)
            self.fields['modelo_notebook'].queryset = Modelos.objects.filter(m_param='03')

    class Meta:
        model = Notebooks
        fields =['serie_notebook','modelo_notebook','estado_notebook','fecha_compra_notebook',
                 'valor_notebook','observaciones_notebook','nram','nhdd','nssd']
        
        widgets = {
            'fecha_compra_notebook' : forms.DateInput(
            format="%d/%m/%Y",attrs={'type':'date','class': 'dtpicker',
                                     'required':"true"}
            )
        }        

class CamionetasForm(forms.ModelForm):

    def __init__(self,*args,**kwargs): ### Filtro de tipo ### 04 Camioneta
            super (CamionetasForm,self ).__init__(*args,**kwargs)
            self.fields['modelo_camioneta'].queryset = Modelos.objects.filter(m_param='04')

    class Meta:
        model = Camionetas
        fields = ['patente','modelo_camioneta','mantencion',
                  'observaciones_camionetas','disponible',
                  'modalidad','vin','kilometraje']

        widgets = {
            'mantencion' : forms.DateTimeInput(
            format="%d/%m/%Y",attrs={'type':'date','class': 'dtpicker',
                                     'required':"true"}
            ),
            'modalidad' : forms.Select(choices=listado_modalidades)
        }  
        
class AsignacionForm(forms.ModelForm):

    class Meta: 
        model = Asignacion
        fields = ['usuario','num','smartphone_a','fecha_sma','tablet_a','fecha_ta',
                  'notebook_a','fecha_nt','camionetas_a','fecha_cm','vigente']
        widgets = {
            'fecha_sma' : forms.DateTimeInput(
            format="%d/%m/%Y",attrs={'type':'date','class': 'dtpicker'}
            ),
            'fecha_ta' : forms.DateTimeInput(
            format="%d/%m/%Y",attrs={'type':'date','class': 'dtpicker'}
            ),
            'fecha_nt' : forms.DateTimeInput(
            format="%d/%m/%Y",attrs={'type':'date','class': 'dtpicker'}
            ),
            'fecha_cm' : forms.DateTimeInput(
            format="%d/%m/%Y",attrs={'type':'date','class': 'dtpicker'}
            ),
        }    

class ProcesadorForm(forms.ModelForm):
     
     class Meta:
          model = Procesador
          fields = {'marca_procesador','modelo_p','ghz','nucleos','año_mf'}

          widgets = {'marca_procesador': forms.Select(choices=listado_procesadores)}

class MantencionesForm(forms.ModelForm):
     
     class Meta:
            model = Mantenciones
            fields = {
               'm_patente','fecha_mantencion','m_kilometraje','m_estado','responsable'
          }
        
            widgets = {
                'fecha_mantencion' : forms.DateTimeInput(
                format="%d/%m/%Y",attrs={'type':'date','class': 'dtpicker','required':'True'}
                )
            }