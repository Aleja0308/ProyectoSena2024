from django.db import models

# Create your models here.

class Basica (models.Model):
  doc = models.IntegerField(default=0)
  tipo_doc = models.CharField(max_length=200)
  nombres = models.CharField(max_length=200)
  apellidos = models.CharField(max_length=200)
  fecha_nacimiento = models.DateField()
  lugar_nacimiento = models.CharField(max_length=200)
  genero = models.CharField(max_length=200)
  edad = models.IntegerField(default=0)
  tipo_sangre = models.CharField(max_length=200) 
  estatura = models.DecimalField(default=0)
  peso = models.DecimalField(default=0)
  ocupacion = models.CharField(max_length=200)
  telefono = models.IntegerField(default=0)
  correo_electronico = models.EmailField()
  direccion_residencia = models.CharField(max_length=200)
  cantidad_hijos = models.IntegerField(default=0)

class Medica (models.Model):
  historial_medico = models.TextField(max_length=500)
  sistematologia_actual = models.TextField(max_length=500)
  medicamentos_actuales = models.TextField(max_length=500)
  examenes_laboratorio = models.TextField(max_length=500)
  examenes_imagenologia = models.TextField(max_length=500)
  antecedentes_familiares = models.TextField(max_length=500)
  antecedentes_personales = models.TextField(max_length=500)
  tension_arterial = models.DecimalField(default=0)
  glucemia = models.DecimalField(default=0)
  sat_O2 = models.IntegerField(default=0)

class Citas (models.Model):
  fecha_cita = models.DateField()
  hora_cita = models.TimeField()
  

