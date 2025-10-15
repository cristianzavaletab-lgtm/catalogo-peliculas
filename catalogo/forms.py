from django import forms
from .models import Genero, Pelicula

class GeneroForm(forms.ModelForm):
    class Meta:
        model = Genero
        fields = ['nombre']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del género'}),
        }
        labels = {
            'nombre': 'Nombre del Género'
        }

class PeliculaForm(forms.ModelForm):
    class Meta:
        model = Pelicula
        fields = ['titulo', 'sinopsis', 'cartel', 'año', 'genero']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título de la película'}),
            'sinopsis': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Sinopsis...'}),
            'año': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Año de estreno'}),
            'genero': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'titulo': 'Título',
            'sinopsis': 'Sinopsis',
            'cartel': 'Cartel (Imagen)',
            'año': 'Año de Estreno',
            'genero': 'Género'
        }