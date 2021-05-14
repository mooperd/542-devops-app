"""Logged-in page routes."""
from flask import Blueprint, flash, redirect, render_template, url_for, request
from flask_login import current_user, login_required, logout_user
from .forms import NewRaceForm, NewBoatForm
from .models import User, BoatRace, Location, BoatType, Boat, db

# Blueprint Configuration
api_bp = Blueprint(
    'api_bp', __name__,
    template_folder='templates',
    static_folder='static',
    url_prefix='/api'
)


def create_race(new_race_dict, current_user):
    existing_race = BoatRace.query.filter_by(name=new_race_dict["name"]).first()
    if existing_race is None:
        print("Form Validated")
        print(new_race_dict)
        race = BoatRace()
        race.name = new_race_dict["name"]
        race.start_location = db.session.query(Location).filter(Location.id == new_race_dict["start_location"]).one()
        race.finish_location = db.session.query(Location).filter(Location.id == new_race_dict["finish_location"]).one()
        race.boat_type = db.session.query(BoatType).filter(BoatType.id == new_race_dict["boat_type"]).one()
        race.start_time = new_race_dict["start_time"]
        race.private = int(new_race_dict["private"])
        race.user = current_user
        db.session.add(race)
        db.session.commit()
        return 
    else:
        return f"Race name {new_race_dict['name']} already taken"


def create_boat(new_boat_dict, current_user, race_id):
    print(f"within create_boat() race id is {race_id}")
    print(new_boat_dict)
    existing_boat = Boat.query.filter_by(name = new_boat_dict["name"]).first()
    if existing_boat is None:
        boat = Boat()
        boat.name = new_boat_dict["name"]
        boat.BoatRace = db.session.query(BoatRace).filter(BoatRace.id == race_id).one()
        boat.user = current_user
        boat.desiredCourse = 0
        boat.started = 0
        boat.isActive = 0
        boat.boatFlags = 0
        db.session.add(boat)
        db.session.commit()
        return
    else:
        return f"Boat name {new_boat_dict['name']} already taken"


@api_bp.route('/race', methods=['GET', 'POST'])
@login_required
def race():
    """
    Race Endpoint
    """
    # TODO: Add json
    if request.method == 'POST':
        # If the request is form data.
        if request.headers['Content-Type'] == 'application/x-www-form-urlencoded':
            print("Content-Type OK")
            form = NewRaceForm()
            if form.validate_on_submit():
                race_output = create_race(form.data, current_user)
                if race_output is None: #success
                    flash( f"Race {form.name.data} created successfully", "is-success")
                    # TODO: Return new race page not the races list?
                    return redirect(url_for('pages_bp.races'))
                else: #fail
                    # TODO: Do we need this extra redirect?
                    flash(race_output, "is-danger")
                    # TODO: This return feels super boilerplate!
                    return redirect(url_for('pages_bp.races'))


@api_bp.route('/boat/?race_id=<race_id>', methods=['GET', 'POST'])
@login_required
def boat(race_id):
    """
    Boat Endpoint
    """
    # TODO: Add json
    if request.method == 'POST':
        # If the request is form data.
        if request.headers['Content-Type'] == 'application/x-www-form-urlencoded':
            print("Content-Type OK")
            form = NewBoatForm()
            if form.validate_on_submit():
                print(f"within boat() race id is {race_id}")
                boat_output = create_boat(form.data, current_user, race_id)
                if boat_output is None:
                    # TODO: Return race page not the dashboard
                    return redirect(url_for('pages_bp.race', race_id=race_id))
                else:
                    flash(boat_output)
                    # TODO: This return feels super boilerplate!
                    return redirect(url_for('pages_bp.race', race_id=race_id))
                    """
                    return render_template(
                        'race.jinja2',
                        title='The race page',
                        template='dashboard-template',
                        current_user=current_user,
                        body="You are now logged in!",
                        race=db.session.query(BoatRace).filter(BoatRace.id == race_id).one(),
                        form=form
                    )
                    """
          


@api_bp.route("/logout")
@login_required
def logout():
    """User log-out logic."""
    logout_user()
    return redirect(url_for('auth_bp.login'))


@api_bp.route("/healthz")
def healthz():
    """Health check"""
    return "OK"

