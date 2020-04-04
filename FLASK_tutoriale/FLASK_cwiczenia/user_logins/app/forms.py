from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
from app.models import User

class LoginForm(FlaskForm):
    username = StringField('Nazwa użytkownika', validators=[DataRequired()])
    password = PasswordField('Hasło', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    username = StringField('Nazwa użytkownika', validators=[DataRequired()])
    email = StringField('Adres e-mail', validators=[DataRequired(), Email()])
    password = PasswordField('Hasło', validators=[DataRequired()])
    password2 = PasswordField('Powtórz hasło', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Zarejestruj się')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Ta nazwa użytkownika jest już zajęta.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Ten adres e-mail jest już zarejestrowany.')


