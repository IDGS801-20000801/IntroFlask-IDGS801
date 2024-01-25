from wtforms import Form
from wtforms import StringField, TelField

class UserForm(form):
    nombre = StringField('nombre')
    email = StringField('email')
    a_paterno = StringField('apaterno')
    a_materno = StringField('amaterno')