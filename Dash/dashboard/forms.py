from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Field, HTML
from django import forms
from localflavor.cl.forms import CLRutField

from . import models

class UserForm(forms.ModelForm):
    """
    Formulario Usuario
    """
    class meta:
        model = models.Usuarios
        fields = [
            'rut',
            'nombre',
            'apellido',
            'area',
            'correo',
            'telefono',

        ]

def __init__(self,*args,**kwargs):
    super(UserForm,self).__init__(*args,**kwargs)
    self.helper = FormHelper()
    self.helper.form_id = 'id-UserForm'
    self.helper.form_method = 'post'
    self.helper.form_action = '.'
    self.helper.layout = Layout(
        'id_UserForm',
        'rut',
        'nombre',
        'apellido',
        'area',
        'correo',
        'telefono',

              HTML(
                "<br>"
                "<div class='text-center'>"
                "<div class='btn-group'>"
                "<a href='{% url 'directorio:Usuarios' %}' class='btn btn-lg btn-dark'>"
                "<i class='fa fa-arrow-left'></i> "
                "Volver</a>"
                "<button type='submit' class='btn btn-lg btn-success'>"
                "<i class='fa fa-save'></i> "
                "Guardar </button>"
                "</div>"
                "</div>"
            )
        
    )