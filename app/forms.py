#Add any form classes for Flask-WTF here
from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,PasswordField
from wtforms.validators import InputRequired,DataRequired
from wtforms import FileField
from flask_wtf.file import FileRequired,FileAllowed

class MovieForm(FlaskForm):
    title=StringField('Title', validators=[InputRequired()])
    description=TextAreaField('Description', validators=[DataRequired()])
    poster= FileField('Poster', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!')])