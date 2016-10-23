from flask_security.forms import RegisterForm, StringField, Required

class ExtendedRegisterForm(RegisterForm):
    first_name = StringField('First Name', [Required('First Name not provided')])
    last_name = StringField('Last Name', [Required('Last Name not provided')])