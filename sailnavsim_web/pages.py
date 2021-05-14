"""Logged-in page routes."""
from flask import Blueprint, redirect, render_template, url_for, request
from flask_login import current_user, login_required, logout_user
from .forms import NewRaceForm, NewBoatForm
from .models import User, BoatRace, BoatType, Location, Boat, db

# Blueprint Configuration
pages_bp = Blueprint(
    'pages_bp', __name__,
    template_folder='templates',
    static_folder='static',
    url_prefix='/pages'
)

@pages_bp.route('/races', methods=['GET'])
@login_required
def races():
    """New Race Form"""
    form = NewRaceForm()
    races = []
    # Get races and users from the database and slap them together into a single list of dicts.
    # for race, user in db.session.query(BoatRace, User).filter(User.id == BoatRace.user_id).all():
    #     races.append({"race": race, "user": user })
    races = races=db.session.query(BoatRace).all()
    for race in races:
        print(race.user.name)
        print(race.start_location.name)
    return render_template(
        'races.jinja2',
        title='New Race Form',
        template='dashboard-template',
        current_user=current_user,
        body="You are now logged in!",
        races=races,
        form=form,
        # choices=[(b.id, b.name) for b in BoatType.query.order_by('name').all()]
    )


@pages_bp.route('/race/<race_id>', methods=['GET'])
@login_required
def race(race_id):
    """Race View and New Boat Form"""
    form = NewBoatForm()
    return render_template(
        'race.jinja2',
        title='The race page',
        template='dashboard-template',
        current_user=current_user,
        body="You are now logged in!",
        race=db.session.query(BoatRace).filter(BoatRace.id == race_id).one(),
        boats=db.session.query(Boat).filter(Boat.BoatRace_id == race_id).all(),
        form=form
    )


@pages_bp.route('/test_page', methods=['GET'])
@login_required
def test():
    """This is a test page"""
    form = TestForm()
    return render_template(
        'test.jinja2',
        title='Test Page',
        template='dashboard-template',
        current_user=current_user,
        body="You are now testing!",
        form=form
    )
    

@pages_bp.route('/boat', methods=['GET'])
@login_required
def boat():
    """Logged-in User Dashboard."""
    return render_template(
        'boat.jinja2',
        title='Boat Page Title',
        template='dashboard-template',
        current_user=current_user,
        message="You are now logged in!"
    )


@pages_bp.route("/logout")
@login_required
def logout():
    """User log-out logic."""
    logout_user()
    return redirect(url_for('auth_bp.login'))