from django import forms
from .models import *
import re
from django.core.exceptions import ValidationError

listado_areas =(
    ('Administracion','Administracion'),
    ('Terreno','Terreno'),
    )

listado_sucursales =(
    ('Bulnes','Bulnes'),
    ('Talca','Talca'),
    ('Chillan','Chillan'),
    ('Peru','Peru'),
)

class EstadosForm(forms.ModelForm):
    class Meta:
        model = Estados
        fields = ['e_equipos']

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = ['rut', 'nombre','apellido','area', 'correo']

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
    class Meta:
        model = Smartphones
        fields = ['serie_smartphone','modelo_smartphone',
                  'imei1','imei2','estado_telefono','fecha_compra_telefono',
                  'valor_telefono','observaciones_telefonos']
        
        widgets = {
            'fecha_compra_telefono' : forms.DateTimeInput(
            format="%d/%m/%Y",attrs={'type':'date','class': 'dtpicker',
                                     'required':"true"}
            )
        }

###### Prueba de filtro por tipo ##### no funcional actualmente
        def __init__(self,*args,**kwargs): 
            super (SmartphonesForm,self ).__init__(*args,**kwargs)
            self.fields['modelo_smartphone'].queryset = Modelos.objects.filter(name__icontains="Smartphone")

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
        fields = ['m_marca','m_param','m_modelo']

class TabletsForm(forms.ModelForm):
    class Meta:
        model = Tablets
        fields = ['serie_tablet','modelo_tablet','imei_tb','estado_tablet','fecha_compra_tablet',
                  'valor_tablet','observaciones_tablets']
        
        widgets = {
            'fecha_compra_tablet' : forms.DateTimeInput(
            format="%d/%m/%Y",attrs={'type':'date','class': 'dtpicker',
                                     'required':"true"}
            )
        }        

class NotebooksForm(forms.ModelForm):
    class Meta:
        model = Notebooks
        fields =['serie_notebook','modelo_notebook','estado_notebook','fecha_compra_notebook',
                 'valor_notebook','observaciones_notebook']
        
        widgets = {
            'fecha_compra_notebook' : forms.DateTimeInput(
            format="%d/%m/%Y",attrs={'type':'date','class': 'dtpicker',
                                     'required':"true"}
            )
        }        

class CamionetasForm(forms.ModelForm):
    class Meta:
        model = Camionetas
        fields = ['patente','modelo_camioneta','mantencion',
                  'observaciones_camionetas','disponible']

        widgets = {
            'mantencion' : forms.DateTimeInput(
            format="%d/%m/%Y",attrs={'type':'date','class': 'dtpicker',
                                     'required':"true"}
            )
        }        
        
class AsignacionForm(forms.ModelForm):
    class Meta:
        model = Asignacion
        fields = ['usuario','num','smartphone_a','fecha_sma','tablet_a','fecha_ta',
                  'notebook_a','fecha_nt','camionetas_a','fecha_cm','vigente']

        widgets = {
            'fecha_sma' : forms.DateTimeInput(
            format="%d/%m/%Y",attrs={'type':'date','class': 'dtpicker',
                                     'required':"true"}
            ),
            'fecha_ta' : forms.DateTimeInput(
            format="%d/%m/%Y",attrs={'type':'date','class': 'dtpicker',
                                     'required':"true"}
            ),
            'fecha_nt' : forms.DateTimeInput(
            format="%d/%m/%Y",attrs={'type':'date','class': 'dtpicker',
                                     'required':"true"}
            ),
            'fecha_cm' : forms.DateTimeInput(
            format="%d/%m/%Y",attrs={'type':'date','class': 'dtpicker',
                                     'required':"true"}
            )
        }     

#marcas y modelos, respaldo poco eficiente#         

'''class Marcas_sm_form(forms.ModelForm):
    class Meta:
        model =Marcas_smartphones
        fields = ['marcas_sm']

class Modelos_sm_form(forms.ModelForm):
    class Meta:
        model = Modelos_smartphones
        fields = ['marca_sm','modelo_sm']

class Marcas_tablets_forms(forms.ModelForm):
    class Meta:
        model = Marcas_tablets
        fields = ['marcas_tb']

class Modelos_tablets_forms(forms.ModelForm):
    class Meta:
        model = Modelos_tablets
        fields = ['marca_tb','modelo_tb']
    
class Marcas_notebook_forms(forms.Modelform):
    class Meta:
        model = Marcas_notebook
        fields = ['marcas_nt']

class Modelos_notebook_forms(forms.ModelForm):
    class Meta:
        model = Modelos_notebook
        fields = ['marca_nt','modelo_nt']

class Marcas_camionetas_forms(forms.Modelform):
    class Meta:
        model = Marcas_camionetas
        fields = ['marcas_cm']

class Modelos_camionetas_forms(forms.ModelForm):
    class Meta:
        model = Modelos_camionetas
        fields = ['marca_cm','modelo_cm']




'''
 #sin uso #
#class series_form(forms.ModelForm): #
#    class Meta:
#        model = Series
#        fields = ['id','serie','fecha_compra','valor','imei_1','imei_2']