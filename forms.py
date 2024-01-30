from wtforms import Form
# Aquí los validadores importamos el dato obligatorio y el email
from wtforms import StringField, EmailField, IntegerField

class UserForm(Form):
    nombre = StringField('nombre')
    a_paterno = StringField('apaterno')
    a_materno = StringField('amaterno')
    email = EmailField('email')
    edad = IntegerField('edad')