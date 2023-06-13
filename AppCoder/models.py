from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField(default=10000)
    fecha_create = models.DateTimeField(auto_created=True, null=True)
    fecha_update = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f"Nombre: {self.nombre}, Camada: {self.camada}"

class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    fecha_alta = models.DateTimeField(auto_created=True, null=True)

    def __str__(self):
        return f"Nombre: {self.nombre}, Apellido: {self.apellido}"

class Profesor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    profesion = models.CharField(max_length=30)
    fecha_alta = models.DateTimeField(auto_created=True, null=True)

    def __str__(self):
        return f"Nombre: {self.nombre}, Apellido: {self.apellido} - Email: {self.email} - Profesion: {self.profesion}"

class Entregable(models.Model):
    nombre = models.CharField(max_length=30)
    fecha_de_Entrega = models.DateTimeField()
    entregado = models.BooleanField()

    def __str__(self):
        return f"Nombre: {self.nombre}, Fecha_de_Entrega: {self.fecha_de_Entrega}, Entregado: {self.entregado}"
