from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class RegistrationForm(FlaskForm):
    username = StringField( 'User Name' )
    email = StringField( 'Email', validators = [DataRequired(), Email()])
    password = PasswordField( 'Password', validators = [DataRequired()])
    confirm_password = PasswordField( 'Re-enter Password', validators = [ DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')