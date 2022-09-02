from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, ValidationError

from main.modules import User


class RegistrationForm (FlaskForm):
    firstname = StringField ('Firstname',
                             validators=[DataRequired (), Length (min=2, max=20)])
    lastname = StringField ('Lastname',
                            validators=[DataRequired (), Length (min=2, max=20)])
    email = StringField ('Email',
                         validators=[DataRequired (), Email ()])
    reference_code = StringField ('Reference Code',
                                  validators=[DataRequired (), Length (min=6, max=20)])

    submit = SubmitField ('Sign Up')

    def validate_field(self, email_address):

        user = User.query.filter_by(email_address=email_address.data).first()
        if user:
            raise ValidationError('That Email is taken, please use another')


class LoginForm (FlaskForm):
    email = StringField ('Email',
                         validators=[DataRequired (), Email ()])
    submit = SubmitField ('Login')
