from django.contrib import admin
from .models import Genero, Pelicula

@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre']
    search_fields = ['nombre']

@admin.register(Pelicula)
class PeliculaAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'año', 'genero']
    list_filter = ['genero', 'año']
    search_fields = ['titulo', 'sinopsis']