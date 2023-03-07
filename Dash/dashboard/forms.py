from django import forms
from .models import *
import re
from django.core.exceptions import ValidationError
    
class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = ['rut', 'nombre','apellido','area', 'correo']

class DepartamentoForm(forms.ModelForm):
    class Meta:
        model = Departamentos
        fields = ['id','area','sucursal']

class TelefonoForm(forms.ModelForm):
    class Meta:
        model = Num_telefono
        fields = ['numero_tel','activo']

class SmartphonesForm(forms.ModelForm):
    class Meta:
        model = Smartphones
        fields = ['serie_smartphone','modelo_smartphone',
                  'imei1','imei2','estado_telefono','fecha_compra_telefono',
                  'valor_telefono','funciona_telefono','observaciones_telefonos']

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
        fields = ['serie_tablet','modelo_tablet','imei_tb','fecha_compra_tablet',
                  'valor_tablet','observaciones_tablets']

class NotebooksForm(forms.ModelForm):
    class Meta:
        model = Notebooks
        fields =['serie_notebook','modelo_notebook','fecha_compra_notebook',
                 'valor_notebook','observaciones_notebook']

class CamionetasForm(forms.ModelForm):
    class Meta:
        model = Camionetas
        fields = ['patente','modelo_camioneta','mantencion',
                  'observaciones_camionetas']        
        
class AsignacionForm(forms.ModelForm):
    class Meta:
        model = Asignacion
        fields = ['usuario','num','smartphone_a','tablet_a',
                  'notebook_a','camionetas_a','vigente']

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