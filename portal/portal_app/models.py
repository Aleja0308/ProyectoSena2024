from django.db import models

# Create your models here.

#Se define modelos Documento:
class Documento(models.Model):
  tipo_doc = models.CharField(max_length=20)

#Se define modelos Genero:
class Genero(models.Model):
  genero = models.CharField(max_length=20)

#Se define modelos Sangre:
class Sangre(models.Model):
  tipo_sangre = models.CharField(max_length=20)

#Se define modelos Hijos:
class Hijos(models.Model):
  can_hijos = models.CharField(max_length=20)

#Se define modelos Estado:
class Estado(models.Model):
  estado_civil = models.CharField(max_length=20)

#Se define modelos Ocupacion:
class Ocupacion(models.Model):
  ocupacion = models.CharField(max_length=20)


#Se define modelos Basica:

class Basica (models.Model):
  nombres = models.CharField(max_length=100, verbose_name="Nombres")
  apellidos = models.CharField(max_length=100, verbose_name="Apellidos")
  fecha_nacimiento = models.DateField(verbose_name="Fecha de nacimiento")
  lugar_nacimiento = models.CharField(max_length=100, verbose_name="Lugar de nacimiento")
  edad = models.IntegerField(verbose_name="Edad")
  estatura = models.FloatField(verbose_name="Estatura")
  peso = models.FloatField(verbose_name="Peso")
  telefono = models.IntegerField(verbose_name="Teléfono")
  correo_electronico = models.EmailField(verbose_name="Correo electrónico")
  direccion_residencia = models.CharField(max_length=100, verbose_name="Dirección de residencia")
  #De definen llaves foráneas:
  documento = models.ForeignKey(Documento, on_delete = models.PROTECT)
  genero = models.ForeignKey(Genero, on_delete = models.PROTECT)
  sangre = models.ForeignKey(Sangre, on_delete = models.PROTECT)
  hijos = models.ForeignKey(Hijos, on_delete = models.PROTECT)  
  estado = models.ForeignKey(Estado, on_delete = models.PROTECT)
  ocupacion = models.ForeignKey(Ocupacion, on_delete = models.PROTECT)


#Se define modelos Medica:

class Medica (models.Model):
  historial_medico = models.TextField(max_length=250, verbose_name="Historial médico")
  sistematologia_actual = models.TextField(max_length=250, verbose_name="Sistematología actual")
  medicamentos_actuales = models.TextField(max_length=250, verbose_name="Medicamentos actuales")
  examenes_laboratorio = models.TextField(max_length=250, verbose_name="Exámenes de laboratorio")
  examenes_imagenologia = models.TextField(max_length=250, verbose_name="Exámenes imagenología")
  antecedentes_familiares = models.TextField(max_length=250, verbose_name="Antecedentes familiares")
  antecedentes_personales = models.TextField(max_length=250, verbose_name="Antecedentes personales")
  tension_arterial = models.FloatField(verbose_name="Tensión arterial")
  glucemia = models.FloatField(verbose_name="Glucemia")
  sat_O2 = models.IntegerField(verbose_name="Saturación O2")