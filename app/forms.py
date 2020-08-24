from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField,
                     BooleanField, SubmitField, IntegerField,)
from wtforms.validators import (
    ValidationError, Regexp, DataRequired, Email, EqualTo, Length,)
from app.models import Admin, Employee


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField(
        'Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_email(self, email):
        user = Admin.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')


class EmpForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Phone', validators=[
        DataRequired(), Regexp('^[0-9]{10}$', message="Only 10 Digits")])
    name = StringField('Name', validators=[
        DataRequired(), Length(min=2, max=50)])
    location = StringField('Location', validators=[
        DataRequired(), Length(min=2, max=50)])
    salary = IntegerField('Salary (Rs)', validators=[
        DataRequired()])

    submit = SubmitField('Add Employee')

    def validate_email(self, email):
        user = Employee.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')

    def validate_phone(self, phone):
        user = Employee.query.filter_by(phone=phone.data).first()
        if user is not None:
            raise ValidationError('Please use a different phone number')


class UpdateEmpForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Phone', validators=[
        Regexp('^[0-9]{10}$', message="Only 10 Digits"), DataRequired()])
    name = StringField('Name', validators=[
        DataRequired(), Length(min=2, max=50)])
    location = StringField('Location', validators=[
        DataRequired(), Length(min=2, max=50)])
    salary = IntegerField('Salary (Rs)', validators=[
        DataRequired()])

    submit = SubmitField('Update Employee')
