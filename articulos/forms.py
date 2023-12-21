
from django import forms
from .models import Comentario
from .models import Articulo

class FormularioComentario(forms.ModelForm):
     class Meta:#configurar el comportamiento de la clase 
         model=Comentario
         fields=('comentario',)


class FiltroArticulosForm(forms.Form):
    plataformas = Articulo.objects.values_list('plataforma', flat=True).distinct()
    generos = Articulo.objects.values_list('genero', flat=True).distinct()
    modalidades = Articulo.objects.values_list('modalidad', flat=True).distinct()

    plataforma = forms.ChoiceField(choices=[(plataforma, plataforma) for plataforma in plataformas], required=False)
    genero = forms.ChoiceField(choices=[(genero, genero) for genero in generos], required=False)
    modalidad = forms.ChoiceField(choices=[(modalidad, modalidad) for modalidad in modalidades], required=False)
