from django import forms
from .models import Publicar

class PostearForm(forms.ModelForm):
    #Se define como va a ser el formulario
    class Meta:
        model = Publicar
        fields = ('titulo', 'texto',)
