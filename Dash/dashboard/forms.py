from django import forms
from .models import *

class nombre_usuario(forms.Form):
    your_name = forms.CharField(label='nombre_usuario', max_length=20)
    
class usuario_form(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = ['rut', 'nombre','area', 'correo', 'Telefono']
