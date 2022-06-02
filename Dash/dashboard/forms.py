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

    def validar_rut(self):
        super(usuario_form, self).clean()
        data = self.cleaned_data['rut']
        x = re.search("[0-9]{8}[0-9kK]{1}$", data)
        if x == False:
            #raise forms.ValidationError('rut no valido')
            print('rut')
            print(x)
            self.errors['rut'] = self.error_class(['caracteres invalidos ingresados'])
        else:
            print('rut')
            print(x)
            return self.cleaned_data
            
        
        
        
        
        
        #super(usuario_form, self).clean()
        #rut = self.cleaned_data.get('rut')
        #txt = usuario.rut
        #x = re.search("[0-9]{8}[0-9kK]{1}$", rut)
        #if not x:
        #    raise forms.ValidationError('rut no valido')
        #else:
        #    return super().validar_rut(form)
            