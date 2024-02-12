from flask_wtf import FlaskForm
from wtforms import validators
from wtforms.fields import *


class JoinGroupForm(FlaskForm):
    group_id = HiddenField("Group ID")
    submit = SubmitField("Join", render_kw={"class": "btn-success"})


class LeaveGroupForm(FlaskForm):
    group_id = HiddenField("Group ID")
    submit = SubmitField("Leave", render_kw={"class": "btn-danger"})


class ProfileForm(FlaskForm):
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    phone = StringField('Phone Number')
    submit = SubmitField()


class GroupForm(FlaskForm):
    title = StringField('Title')
    submit = SubmitField()


class LoginForm(FlaskForm):
    email = EmailField('Email Address', [
        validators.DataRequired(),
    ])

    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.length(min=6, max=35)
    ])
    submit = SubmitField()


class RegisterForm(FlaskForm):
    email = EmailField('Email Address', [
        validators.DataRequired(),

    ], description="You need to signup with an email")

    password = PasswordField('Create Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match'),

    ], description="Create a password ")
    confirm = PasswordField('Repeat Password', description="Please retype your password to confirm it is correct")
    submit = SubmitField()
