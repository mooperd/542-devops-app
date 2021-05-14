"""Sign-up & log-in forms."""
import arrow
from flask_wtf import FlaskForm
from wtforms import SelectField, PasswordField, StringField, SubmitField, DecimalField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Optional, IPAddress
from .models import BoatType, Location, db
# from wtforms.ext.sqlalchemy.fields import QuerySelectField


def boat_type_choices():
    print("running boat_type_choices()")
    output_list = []
    result = db.session.query(BoatType).all()
    for row in result:
        output_list.append((row.id, row.name))
    return output_list


def location_choices():
    print("running location_choices()")
    output_list = []
    result = db.session.query(Location).all()
    for row in result:
        output_list.append((row.id, row.name))
    return output_list


def get_now_time_plus_10():
    output = arrow.now().int_timestamp + 10
    return output


class SignupForm(FlaskForm):
    """User Sign-up Form."""
    name = StringField(
        'Name',
        validators=[DataRequired()]
    )
    email = StringField(
        'Email',
        validators=[
            Length(min=6),
            Email(message='Enter a valid email.'),
            DataRequired()
        ]
    )
    password = PasswordField(
        'Password',
        validators=[
            DataRequired(),
            Length(min=6, message='Select a stronger password.')
        ]
    )
    confirm = PasswordField(
        'Confirm Your Password',
        validators=[
            DataRequired(),
            EqualTo('password', message='Passwords must match.')
        ]
    )
    website = StringField(
        'Website',
        validators=[Optional()]
    )
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    """User Log-in Form."""
    email = StringField(
        'Email',
        validators=[
            DataRequired(),
            Email(message='Enter a valid email.')
        ]
    )
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')


class NewRaceForm(FlaskForm):

    # Fill in choices and defaults
    def __init__(self, *args, **kwargs):
        locations = location_choices()
        self.start_location.kwargs['choices'] = locations
        self.finish_location.kwargs['choices'] = locations
        self.boat_type.kwargs['choices'] = boat_type_choices()
        self.start_time.kwargs['default'] = get_now_time_plus_10()
        super().__init__(*args, **kwargs)

    """Information required to start a new race"""
    name = StringField('name', validators=[DataRequired(), ])
    start_location = SelectField('Start Location', validators=[DataRequired(), ])
    finish_location = SelectField('Finish Location', validators=[DataRequired(), ])
    boat_type = SelectField('Boat Type', validators=[DataRequired(), ])
    start_time = IntegerField('Start Time', validators=[DataRequired(), ])
    private = BooleanField('private', validators=[DataRequired(), ])
    submit = SubmitField('Submit')


class NewBoatForm(FlaskForm):
    """Information required to start a new race"""
    name = StringField('name', validators=[DataRequired(), ])
    submit = SubmitField('Create Boat!')


class TestForm(FlaskForm):
    """This is a test form"""
    name = StringField('name', validators=[DataRequired(), ])
    email = StringField('Email', validators=[DataRequired(),  Email(message='Enter a valid email.')])
    submit = SubmitField('Log In')
