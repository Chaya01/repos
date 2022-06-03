from django import forms
from .models import *
import re
from django.core.exceptions import ValidationError

class nombre_usuario(forms.Form):
    your_name = forms.CharField(label='nombre_usuario', max_length=20)
    
class usuario_form(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = ['rut', 'nombre','apellido','area', 'correo', 'telefono']

class departamento_form(forms.ModelForm):
    class Meta:
        model = Departamentos
        fields = ['id','area','sucursal']

class telefono_form(forms.ModelForm):
    class Meta:
        model = Num_telefono
        fields = ['id','numero_tel','activo']