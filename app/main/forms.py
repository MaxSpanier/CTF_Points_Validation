from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, InputRequired

class FlagForm(FlaskForm):
    flag = StringField("Flag", validators=[DataRequired()])

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired()])
    username = PasswordField("Password", validators=[InputRequired()])