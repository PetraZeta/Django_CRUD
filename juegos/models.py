from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=100 , unique=True)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Disenador(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    nacionalidad = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Juego(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_lanzamiento = models.DateField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    disenador = models.ForeignKey(Disenador, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='imagenes/', null=True, blank=True)

    def __str__(self):
        return self.nombre

class Resena(models.Model):
    juego = models.ForeignKey(Juego, on_delete=models.CASCADE , related_name='resenas')
    calificacion = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], 
                                       validators=[MinValueValidator(1), MaxValueValidator(5)
                                                   ])
    comentario = models.TextField()

    def __str__(self):
        return f"{self.juego.nombre} - {self.calificacion}"