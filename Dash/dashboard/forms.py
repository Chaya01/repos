from django import forms

class nombre_usuario(forms.Form):
    your_name = forms.CharField(label='nombre_usuario', max_length=20)