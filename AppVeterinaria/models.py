from django.db import models

# Create your models here.


class Animal(models.Model):
    nombreAnimal = models.CharField(max_length=40)
    edad = models.IntegerField()
    tipo = models.CharField(max_length=40)
    motivo = models.CharField(max_length=40)
    fecha = models.DateField()
    costo = models.IntegerField()

    def __str__(self):
        return f"Nombre: {self.nombreAnimal} - Edad: {self.edad} - Tipo: {self.tipo} - Motivo: {self.motivo} - Fecha: {self.fecha} - Costo: {self.costo} "


class Veterinario(models.Model):
    veterinario = models.CharField(max_length=20)
    apellidoVet = models.CharField(max_length=40)
    matricula = models.CharField(max_length=40)

    def __str__(self):
        return f"Veterinario: {self.veterinario} - ApellidoVet: {self.apellidoVet} - Matricula: {self.matricula}"


class Persona(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    telefono = models.IntegerField()

    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - Telefono: {self.telefono} "
