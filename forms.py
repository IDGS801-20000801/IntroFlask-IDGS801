from wtforms import Form
# Aquí los validadores importamos el dato obligatorio y el email
from wtforms import StringField, EmailField, IntegerField

class UserForm(Form):
    nombre = StringField('Nombre')
    a_paterno = StringField('Primer Apellido')
    a_materno = StringField('Segundo Apellido')
    email = EmailField('Email')
    edad = IntegerField('Edad')