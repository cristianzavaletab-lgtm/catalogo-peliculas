from django.db import models

class Genero(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Género"
        verbose_name_plural = "Géneros"

class Pelicula(models.Model):
    titulo = models.CharField(max_length=200)
    sinopsis = models.TextField()
    cartel = models.CharField(max_length=500)
    año = models.IntegerField()
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.titulo} ({self.año})"
    
    class Meta:
        verbose_name = "Película"
        verbose_name_plural = "Películas"