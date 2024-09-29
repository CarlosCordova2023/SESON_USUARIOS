from django import forms

from .models import Libro

class LibroForm(forms.Form):
    titulo = forms.CharField(max_length=150, required=True, label='Título')
    autor = forms.CharField(max_length=150, required=True, label='Autor')
    valoracion = forms.IntegerField(min_value=0, max_value=10000, required=True, label='Valoración')


class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'autor', 'valoracion']