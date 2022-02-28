from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField
from wtforms.validators import DataRequired

class PhotoForm(FlaskForm):
    photo = FileField('Photo', validators = [FileRequired(), FileAllowed(['jpg', 'jpeg', 'png', 'Images Only!'])])
