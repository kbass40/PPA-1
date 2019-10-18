from flask_wtf import FlaskForm
from wtforms import IntegerField, FloatField, SubmitField, StringField
from wtforms.validators import DataRequired

class BMIForm(FlaskForm):
    footField = IntegerField('Feet', validators=[DataRequired()])
    inchesField = IntegerField('Inches', validators=[DataRequired()])
    poundsField = FloatField('Pounds', validators=[DataRequired()])
    submit = SubmitField('POST')

class EmailForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    submit = SubmitField('POST')
