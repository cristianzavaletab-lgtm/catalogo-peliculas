from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    
    # URLs para Géneros
    path('generos/', views.GeneroListView.as_view(), name='genero_list'),
    path('generos/nuevo/', views.GeneroCreateView.as_view(), name='genero_create'),
    path('generos/editar/<int:pk>/', views.GeneroUpdateView.as_view(), name='genero_update'),
    path('generos/eliminar/<int:pk>/', views.GeneroDeleteView.as_view(), name='genero_delete'),
    
    # URLs para Películas
    path('peliculas/', views.PeliculaListView.as_view(), name='pelicula_list'),
    path('peliculas/nueva/', views.PeliculaCreateView.as_view(), name='pelicula_create'),
    path('peliculas/editar/<int:pk>/', views.PeliculaUpdateView.as_view(), name='pelicula_update'),
    path('peliculas/eliminar/<int:pk>/', views.PeliculaDeleteView.as_view(), name='pelicula_delete'),
    path('peliculas/<int:pk>/', views.PeliculaDetailView.as_view(), name='pelicula_detail'),
]