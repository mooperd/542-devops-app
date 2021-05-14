"""Database models."""
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash
from . import db


class User(UserMixin, db.Model):
    """User account model."""

    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=False)
    email = db.Column(db.String(40), unique=True, nullable=False)
    password = db.Column(db.String(200), primary_key=False, unique=False, nullable=False)
    website = db.Column(db.String(60), index=False, unique=False, nullable=True)
    created_on = db.Column(db.DateTime, index=False, unique=False, nullable=True)
    last_login = db.Column(db.DateTime, index=False, unique=False, nullable=True)

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method='sha256')

    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<User {}>'.format(self.name)

class BoatType(db.Model):
    __tablename__   = 'BoatType'
    id              = db.Column(db.Integer, primary_key=True, unique=True)
    name            = db.Column(db.String(20), nullable=False, unique=True)

class Boat(db.Model):
    __tablename__   = 'Boat'
    id              = db.Column(db.Integer, primary_key=True, unique=True)
    name            = db.Column(db.String(20), nullable=False, unique=True)
    desiredCourse   = db.Column(db.Float, nullable=False)
    started         = db.Column(db.Integer, nullable=False)
    isActive        = db.Column(db.Integer, nullable=False)
    boatFlags       = db.Column(db.Integer, nullable=False)
    BoatRace        = db.relation("BoatRace")
    BoatRace_id     = db.Column(db.Integer, db.ForeignKey('BoatRace.id'), nullable=False)
    user            = db.relation("User")
    user_id         = db.Column(db.Integer, db.ForeignKey('Users.id'), nullable=False)


class Location(db.Model):
    __tablename__   = 'Location'
    id              = db.Column(db.Integer, primary_key=True)
    name            = db.Column(db.String(20), nullable=False, unique=True)
    start_lat       = db.Column(db.Float, nullable=False)
    start_lon       = db.Column(db.Float, nullable=False)
    sw_corner_lat   = db.Column(db.Float, nullable=False)
    sw_corner_lon   = db.Column(db.Float, nullable=False)
    ne_corner_lat   = db.Column(db.Float, nullable=False)
    ne_corner_lon   = db.Column(db.Float, nullable=False)
    user            = db.relation("User")
    user_id         = db.Column(db.Integer, db.ForeignKey('Users.id'), nullable=False)


class BoatRace(db.Model):
    __tablename__   = 'BoatRace'
    id              = db.Column(db.Integer, primary_key=True)
    name            = db.Column(db.String(20), nullable=False, unique=True)
    boat_type       = db.Column(db.Integer, nullable=False)
    start_time      = db.Column(db.Integer, nullable=False)
    private         = db.Column(db.Integer, nullable=False)
    boat_type_id    = db.Column(db.Integer, db.ForeignKey('BoatType.id'), nullable=False)
    boat_type       = db.relation("BoatType") 
    start_loc_id    = db.Column(db.Integer, db.ForeignKey('Location.id'), nullable=False)
    start_location  = db.relation("Location", foreign_keys='BoatRace.start_loc_id')
    finish_loc_id   = db.Column(db.Integer, db.ForeignKey('Location.id'), nullable=False)
    finish_location = db.relation("Location", foreign_keys='BoatRace.finish_loc_id')
    user_id         = db.Column(db.Integer, db.ForeignKey('Users.id'), nullable=False)
    user            = db.relation("User")



class BoatLog(db.Model):
    __tablename__   = 'BoatLog'
    __table_args__ = (
        db.UniqueConstraint('boat_id', 'time', name='unique_boat_id_time'),
    )
    time            = db.Column(db.Integer, nullable=False)
    lat             = db.Column(db.Float, nullable=False)
    lon             = db.Column(db.Float, nullable=False)
    courseWater     = db.Column(db.Float, nullable=False)
    speedWater      = db.Column(db.Float, nullable=False)
    trackGround     = db.Column(db.Float, nullable=False)
    speedGround     = db.Column(db.Float, nullable=False)
    windDir         = db.Column(db.Float, nullable=False)
    windSpeed       = db.Column(db.Float, nullable=False)
    oceanCurrentDir = db.Column(db.Float)
    oceanCurrentSpeed = db.Column(db.Float)
    waterTemp       = db.Column(db.Float)
    temp            = db.Column(db.Float, nullable=False)
    dewpoint        = db.Column(db.Float, nullable=False)
    pressure        = db.Column(db.Float, nullable=False)
    cloud           = db.Column(db.Integer, nullable=False)
    visibility      = db.Column(db.Integer, nullable=False)
    precipRate      = db.Column(db.Float, nullable=False)
    precipType      = db.Column(db.Integer, nullable=False)
    boatStatus      = db.Column(db.Integer, nullable=False)
    boatLocation    = db.Column(db.Integer, nullable=False)
    waterSalinity   = db.Column(db.Float)
    oceanIce        = db.Column(db.Integer)
    distanceTravelled = db.Column(db.Float, nullable=False)
    damage          = db.Column(db.Float, nullable=False)
    windGust        = db.Column(db.Float, nullable=False)
    waveHeight      = db.Column(db.Float)
    compassMagDec   = db.Column(db.Float, nullable=False)
    invisibleLog    = db.Column(db.Integer, nullable=False)
    boat            = db.relation("Boat")
    boat_id         = db.Column(db.Integer, db.ForeignKey('Boat.id'))

    __mapper_args__ = {
        "primary_key": [boat_id, time]
    }
