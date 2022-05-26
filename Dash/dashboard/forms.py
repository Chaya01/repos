from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Field, HTML
from django import forms
from localflavor.cl.forms import CLRutField

from . import models

class UserForm(form.ModelForm):
    """"""
    Formulario Usuario
    """"""
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