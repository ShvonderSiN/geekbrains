from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, DataRequired, Email, Regexp


class RegistrationForm(FlaskForm):
    username = StringField('Имя пользователя:', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email:', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[
        DataRequired(),
        Length(min=8), Regexp('(?=.*[a-z])(?=.*[0-9])',
                              message="Ошибка! Нужны цифры и буквы!")])
    confirm_password = PasswordField('Подтвердить пароль', validators=[DataRequired(), EqualTo('password')])
    # submit = SubmitField('Зарегистрироваться')


# Homework
class HomeWorkRegistrationForm(FlaskForm):
    name = StringField('Имя пользователя:', validators=[DataRequired(), Length(min=2, max=20)],
                       render_kw={"placeholder": "Имя"})
    surname = StringField('Фамилия:', validators=[DataRequired(), Length(min=1, max=20)],
                          render_kw={"placeholder": "Фамилия"})
    email = StringField('Email:', validators=[DataRequired(), Email()], render_kw={"placeholder": "Email"})
    password = PasswordField('Password', validators=[
        DataRequired(),
        Length(min=8), Regexp('(?=.*[a-z])(?=.*[0-9])',
                              message="Ошибка! Нужны цифры и буквы!")], render_kw={"placeholder": "Пароль"})
    confirm_password = PasswordField('Подтвердить пароль', validators=[DataRequired(), EqualTo('password')],
                                     render_kw={"placeholder": "Подтвердить пароль"})
    submit = SubmitField('Зарегистрироваться')
