from wtforms import Form
# Aquí los validadores importamos el dato obligatorio y el email
from wtforms import StringField, EmailField, IntegerField
from wtforms import validators

class UserForm2(Form):
    nombre = StringField('Nombre', [
        validators.DataRequired(message='This field is requiered'),
        validators.length(min = 4, max = 10, message = 'Insert a valid name')
    ])
    a_paterno = StringField('Primer Apellido')
    a_materno = StringField('Segundo Apellido')
    email = EmailField('Email', [validators.Email(message = 'Insert a valid email')])
    edad = IntegerField('Edad')
    
class UserForm(Form):
    nombre = StringField('nombre', [
        validators.DataRequired(message = 'Campo requerido'),
        validators.length(min=4, max=10, message='Ingresa un nombre valido')
    ])
    primerApellido = StringField('primer apellido')
    segundoApellido = StringField('segundo apellido')
    correo = EmailField('email', [ validators.Email(message='Ingresa un correo valido')])
    edad = IntegerField('edad')