from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField
from wtforms.validators import InputRequired, Email, Length


class MessageForm(FlaskForm):
    """Form for adding/editing messages."""

    text = TextAreaField('text', validators=[InputRequired()])


class UserAddForm(FlaskForm):
    """Form for adding users."""

    username = StringField('Username', validators=[InputRequired(message="username required")])
    email = StringField('E-mail', validators=[InputRequired(message="email required"), Email()])
    password = PasswordField('Password', validators=[Length(min=6)])
    image_url = StringField('(Optional) Image URL')
    

class EditUserForm(FlaskForm):
    """Form for adding users."""

    username = StringField('Username', validators=[InputRequired(message="username required")])
    email = StringField('E-mail', validators=[InputRequired(message="email required"), Email()])
    password = PasswordField('Password', validators=[Length(min=6)])
    image_url = StringField('(Optional) Image URL')
    header_image_url =StringField('(Optional) Header Image URL')
    bio = TextAreaField('(Optional) Enter Bio Here')


class LoginForm(FlaskForm):
    """Login form."""

    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[Length(min=6)])
