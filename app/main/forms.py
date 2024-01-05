from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class FlagForm(FlaskForm):
    flag = StringField("Flag", validators=[DataRequired()])