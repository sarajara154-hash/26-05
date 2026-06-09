from .models import *
from django import forms

class formularioregistro(forms.ModelForm):
    class Meta:
        model=alumnos
        fields="__all__"
        