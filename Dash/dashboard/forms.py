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
        
        
        #super(usuario_form, self).clean()
        #rut = self.cleaned_data.get('rut')
        #txt = usuario.rut
        #x = re.search("[0-9]{8}[0-9kK]{1}$", rut)
        #if not x:
        #    raise forms.ValidationError('rut no valido')
        #else:
        #    return super().validar_rut(form)
            