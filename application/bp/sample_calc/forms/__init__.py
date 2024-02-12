from flask_wtf import FlaskForm
from wtforms import validators
from wtforms.fields import *
from wtforms.validators import InputRequired


class SampleForm(FlaskForm):
    z_score = SelectField('Z Score', coerce=float,
                          choices=[(1.28, '80%'), (1.44, '85%'), (1.65, '90%'), (1.96, '95%'), (2.58, '99%')])
    margin_error = StringField('Margin Error', validators=[InputRequired()])
    std = StringField('Standard Deviation', validators=[InputRequired()])
    population_size = StringField('Population Size', validators=[InputRequired()])
    submit = SubmitField()
