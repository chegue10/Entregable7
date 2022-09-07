from django.db import models

# Create your models here.

class Usuarios(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    dni = models.IntegerField()
    fecha_nacimiento = models.DateField()
    password = models.CharField(max_length=10)
    email = models.EmailField()

class Comentarios(models.Model):
    titulo = models.CharField(max_length=100)
    comentario = models.TextField()
    fecha = models.DateField()
    usuario = models.IntegerField()