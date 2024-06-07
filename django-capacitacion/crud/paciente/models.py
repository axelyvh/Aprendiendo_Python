from django.db import models
import uuid

# Create your models here.
class Paciente(models.Model):
    GENDER = [
        ('masculino', 'masculino'),
        ('femenino', 'femenino'),
    ]

    id = models.UUIDField()
    apellido_P = models.CharField(max_length=50)
    apellido_M = models.CharField(max_length=50)
    nombres = models.CharField(max_length=50)
    genero = models.CharField(choices=GENDER, default='masculino')
    fecha_nac = models.DateField()
    edad = models.IntegerField()