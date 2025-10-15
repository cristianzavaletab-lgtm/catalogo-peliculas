from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Genero, Pelicula
from .forms import GeneroForm, PeliculaForm

# Vistas para la página principal
def home(request):
    return render(request, 'catalogo/home.html')

# Vistas para Géneros
class GeneroListView(ListView):
    model = Genero
    template_name = 'catalogo/genero_list.html'
    context_object_name = 'generos'

class GeneroCreateView(CreateView):
    model = Genero
    form_class = GeneroForm
    template_name = 'catalogo/genero_form.html'
    success_url = reverse_lazy('genero_list')

class GeneroUpdateView(UpdateView):
    model = Genero
    form_class = GeneroForm
    template_name = 'catalogo/genero_form.html'
    success_url = reverse_lazy('genero_list')

class GeneroDeleteView(DeleteView):
    model = Genero
    template_name = 'catalogo/genero_confirm_delete.html'
    success_url = reverse_lazy('genero_list')

# Vistas para Películas
class PeliculaListView(ListView):
    model = Pelicula
    template_name = 'catalogo/pelicula_list.html'
    context_object_name = 'peliculas'

class PeliculaCreateView(CreateView):
    model = Pelicula
    form_class = PeliculaForm
    template_name = 'catalogo/pelicula_form.html'
    success_url = reverse_lazy('pelicula_list')

class PeliculaUpdateView(UpdateView):
    model = Pelicula
    form_class = PeliculaForm
    template_name = 'catalogo/pelicula_form.html'
    success_url = reverse_lazy('pelicula_list')

class PeliculaDeleteView(DeleteView):
    model = Pelicula
    template_name = 'catalogo/pelicula_confirm_delete.html'
    success_url = reverse_lazy('pelicula_list')

class PeliculaDetailView(DetailView):
    model = Pelicula
    template_name = 'catalogo/pelicula_detail.html'
    context_object_name = 'pelicula'