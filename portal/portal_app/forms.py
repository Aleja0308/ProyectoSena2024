from django import forms
from .models import Basica

#Se define el formulario para Basica.

class BasicaForm(forms.ModelForm):

#Se definen opciones Documento:
  DOCUMENTO = [
    ('CC','CC'),
    ('TI','TI'),
    ('RC','RC'),
    ('CE','CE'),
    ('PEP','PEP'),
    ('DNI','DNI'),
    ('SCR','SCR'),
    ('PA','PA')
  ]

  opcion_doc = forms.ChoiceField(choices=DOCUMENTO)
  

#Se definen opciones Genero:
  GENERO = [
    ('FEMENINO','FEMENINO'),
    ('MASCULINO','MASCULINO'),
    ('INDEFINIDO', 'INDEFINIDO'),
    ('OTRO', 'OTRO')
  ]

  opcion_genero = forms.ChoiceField(choices=GENERO)


#Se definen opciones Sangre:
  SANGRE = [
    ('O+','O+'),
    ('O-','O-'),
    ('A+','A+'),
    ('A-','A-'),
    ('B+','B+'),
    ('B-','B-'),
    ('AB+','AB+'),
    ('AB-','AB-'),
  ]

  opcion_sangre = forms.ChoiceField(choices=SANGRE)


#Se definen opciones Hijos:
  HIJOS = [
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5 O MÁS','5 O MÁS')
  ]

  opcion_can_hijos = forms.ChoiceField(choices=HIJOS)


#Se definen opciones Estado:
  ESTADO = [
    ('SOLTERO(A)','SOLTERO(A)'),
    ('UNIÓN LIBRE', 'UNIÓN LIBRE'),
    ('CASADO(A)','CASADO(A)'),
    ('DIVORCIADO(A)','(DIVORCIADO(A)'),
    ('VIUDO(A)','VIUDO(A)')
  ]

  opcion_estado = forms.ChoiceField(choices=ESTADO)


#Se definen opciones Ocupacion:
  OCUPACION = [
    ('DESEMPLEADO','DESEMPLEADO'),
    ('EMPLEADO','EMPLEADO'),
    ('INDEPENDIENTE','INDEPENDIENTE')
  ]

  opcion_ocupacion = forms.ChoiceField(choices=OCUPACION)


  class Meta:
    model = Basica
    fields = [
      'nombres',
      'apellidos',
      'fecha_nacimiento',
      'lugar_nacimiento',
      'edad',
      'estatura',
      'peso',
      'telefono',
      'correo_electronico',
      'direccion_residencia',
      'documento',
      'genero',
      'sangre',
      'hijos',
      'estado',
      'ocupacion'
      ]
    labels = {
      'nombres': 'Nombres',
      'apellidos': 'Apellidos',
      'fecha_nacimiento': 'Fecha de nacimiento',
      'lugar_nacimiento': 'Lugar de nacimiento',
      'edad': 'Edad',
      'estatura': 'Estatura',
      'peso': 'Peso',
      'telefono': 'Teléfono',
      'correo_electronico': 'Correo electrónico',
      'direccion_residencia': 'Direccion residencia',
      'documento' : 'Documento',
      'genero': 'Género',
      'sangre': 'Tipo de sangre',
      'hijos': 'Cantidad de hijos',
      'estado': 'Estado civil',
      'ocupacion': 'Ocupación'
    }
    widgests = {
      'nombres', forms.TextInput(attrs={'type': 'text'}),
      'apellidos', forms.TextInput(attrs={'type': 'text'}),
      'fecha_nacimiento', forms.DateInput(attrs={'type': 'date'}),
      'lugar_nacimiento', forms.TextInput(attrs={'type': 'text'}),
      'edad', forms.NumberInput(attrs={'type': 'number'}),
      'estatura', forms.NumberInput(attrs={'type': 'number'}),
      'peso', forms.NumberInput(attrs={'type': 'number'}),
      'telefono', forms.NumberInput(attrs={'type': 'number'}),
      'correo_electronico', forms.EmailInput(attrs={'type': 'email'}),
      'direccion_residencia', forms.TextInput(attrs={'type': 'text'}),
      'documento', forms.Select(attrs={'class': 'form-control'}),
      'genero', forms.Select(attrs={'class': 'form-control'}),
      'sangre', forms.Select(attrs={'class': 'form-control'}),
      'hijos', forms.Select(attrs={'class': 'form-control'}),
      'estado', forms.Select(attrs={'class': 'form-control'}),
      'ocupacion', forms.Select(attrs={'class': 'form-control'})
    }

#Se define el formulario para Medica.
