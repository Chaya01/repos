from django import forms
from .models import *
import re

class nombre_usuario(forms.Form):
    your_name = forms.CharField(label='nombre_usuario', max_length=20)
    
class usuario_form(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = ['rut', 'nombre','apellido','area', 'correo', 'telefono']

    def validar_rut(self,form):
        super(usuario_form, self).clean()   
        txt = "rut"
        x = re.search("[0-9]{8}[0-9kK]{1}$", txt)
        if bool(x) == True:
            return super().validar_rut(form)
        else:
            raise forms.ValidationError("rut no valido")
