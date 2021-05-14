from .models import db, Boat, BoatType, User, Location, BoatRace
import petname
import random
import arrow

def import_boat_types():
    existing_record = db.session.query(BoatType).first()
    if existing_record is None:
        boats = [
            {"id": 1, "name": "SailNavSim Classic"},
            {"id": 2, "name": "Seascape 18"},
            {"id": 3, "name": "Contessa 25"},
            {"id": 4, "name": "Hanse 385"},
            {"id": 5, "name": "Volvo 70"},
            {"id": 6, "name": "Super Maxi Scallywag"},
            {"id": 7, "name": "140-foot Brigantine"},
            {"id": 8, "name": "Maxi Trimaran"},
            {"id": 9, "name": "IMOCA 60"},
            {"id": 10, "name": "Improvised Lifeboat"}
            ]


        for boat in boats:
            boattype = BoatType()
            boattype.id = boat["id"]
            boattype.name = boat["name"]
            db.session.add(boattype)
            db.session.commit()
            print(f"Boat {boat['name']} Imported!")

def import_users():
    existing_record = db.session.query(User).first()
    if existing_record is None:
        users = [
            {"id": 1, "name": "Andrew Holway", "email": "andrew.holway@gmail.com", "password": "sha256$F2xBXoSW$e57f1b72dcbf6514c797612c0521934f8535034a2dc0c652d345cc811ca26e6a", "website": "https://www.skill-sprint.com"},
            {"id": 2, "name": "Bobby Brown", "email": "bobby.brown@gmail.com", "password": "sha256$F2xBXoSW$e57f1b72dcbf6514c797612c0521934f8535034a2dc0c652d345cc811ca26e6a", "website": "https://www.skill-sprint.com"},
            {"id": 3, "name": "Dick Tracy", "email": "dick.tracy@gmail.com", "password": "sha256$F2xBXoSW$e57f1b72dcbf6514c797612c0521934f8535034a2dc0c652d345cc811ca26e6a", "website": "https://www.skill-sprint.com"}
        ]

        for user in users:
            _user = User()
            _user.name = user["name"]
            _user.email = user["email"]
            _user.password = user["password"]
            _user.website = user["website"]
            db.session.add(_user)
            db.session.commit()
            print(f"User {user['name']} Imported!")

def import_locations():
    existing_record = db.session.query(Location).first()
    if existing_record is None:
        locations = [{
                "name": "Southampton",
                "start": [50.88142493772852, -1.3898281485257344],
                "ne_finish": [50.88643784739628, -1.3781730456654857],
                "se_finish": [50.86036845319887, -1.3755314785821222]
            },
            {
                "name": "Portsmouth",
                "start": [50.82094542619491, -1.1188865901438954],
                "ne_finish": [50.83362607033913, -1.1051562973718594],
                "se_finish": [50.81322670798309, -1.1294948986051552]
            },
            {
                "name": "Brighton",
                "start": [50.80800540225695, -0.10386534494764746],
                "ne_finish": [50.80808800138424, -0.0977837409767864],
                "se_finish": [50.80560034952817, -0.11054090648888935]
            },
            {
                "name": "Margate",
                "start": [51.39185884914584, 1.3733914799398295],
                "ne_finish": [51.394599512451926, 1.373329604988019],
                "se_finish": [51.38753314558722, 1.365033825683924]
            },
            {
                "name": "Southend on Sea",
                "start": [51.530889973900585, 0.7100236012712845],
                "ne_finish": [51.530840155971696, 0.7123353901420538],
                "se_finish": [51.524939495511255, 0.7011748087223475]
            },
            {
                "name": "Harwich",
                "start": [51.9542474709049, 1.2843030169319944],
                "ne_finish": [51.96292820384189, 1.2996446170957632],
                "se_finish": [51.94526795955862, 1.2754090134119278]
            },
            {
                "name": "The Wash",
                "start": [52.90627423050623, 0.28089468459503514],
                "ne_finish": [53.06716231213573, 0.37113022557383096],
                "se_finish": [52.89295274281874, 0.06507153824883367]
            },
            {
                "name": "Hull",
                "start": [53.729306036970925, -0.319428552248649],
                "ne_finish": [53.73906738254316, -0.29277550087242493],
                "se_finish": [53.70905583818828, -0.35883402971191847]
            },
            {
                "name": "Hartlepool",
                "start": [54.62293340044964, -1.1665647160913746],
                "ne_finish": [54.63143235748391, -1.1465240689512026],
                "se_finish": [54.624523870561106, -1.168853317031296]
            },
            {
                "name": "Sunderland",
                "start": [54.9192849609977, -1.3577987631885704],
                "ne_finish": [54.92239671693093, -1.3541314550217756],
                "se_finish": [54.91562661963341, -1.3608150740148512]
            },
            {
                "name": "Newcastle",
                "start": [55.01008868028864, -1.4198557797989775],
                "ne_finish": [55.016585068148466, -1.4085212999479675],
                "se_finish": [55.005540725622325, -1.4230941562841453]
            }
            ]

        user = db.session.query(User).filter(User.id == 1).one()
        for location in locations:
            _location = Location()
            _location.name = location["name"]
            _location.start_lat = location["start"][0]
            _location.start_lon = location["start"][1]
            _location.sw_corner_lat = location["se_finish"][0]
            _location.sw_corner_lon = location["se_finish"][1]
            _location.ne_corner_lat = location["ne_finish"][0]
            _location.ne_corner_lon = location["ne_finish"][1]
            _location.user = user
            db.session.add(_location)
            db.session.commit()
            print(f"Location {location['name']} Imported!")


def import_races():
    # TODO: I did this function drunk...
    def create_race_data():
        data = {  
            "name": petname.Generate(3),
            "boat_type_id": random.randint(1, db.session.query(BoatType).count()),
            "start_time": arrow.now().int_timestamp + 10,
            "private": 1,
            "start_loc_id": random.randint(1, db.session.query(Location).count()),
            "finish_loc_id": random.randint(1, db.session.query(Location).count()),
            "user_id": random.randint(1, db.session.query(User).count())
        }
        return data

    def insert_record():
        race_data = create_race_data()
        boat_race = BoatRace()
        boat_race.name = race_data["name"]
        boat_race.start_time = race_data["start_time"]
        boat_race.boat_type_id = race_data["boat_type_id"]
        boat_race.start_loc_id = race_data["start_loc_id"]
        boat_race.finish_loc_id = race_data["finish_loc_id"]
        boat_race.user_id = race_data["user_id"]
        boat_race.private = race_data["private"]
        db.session.add(boat_race)
        db.session.commit()
        print(f"BoatRace {boat_race.name} Imported with ID {boat_race.id}")

    existing_record = db.session.query(BoatRace).first()
    if existing_record is None:
        for i in range(10):
            insert_record()
            
            


def import_boats():
    # TODO: I did this function drunk...
    def create_boat_data():
        data = {  
            "name": petname.Generate(3),
        }
        return data


    def insert_record(boat_race):
        boat_data = create_boat_data()
        boat = Boat()
        boat.name = boat_data["name"]
        boat.desiredCourse = 0
        boat.started = 0
        boat.isActive = 0
        boat.boatFlags = 0
        boat.BoatRace = boat_race
        boat.user_id = 1
        db.session.add(boat)
        db.session.commit()
        print(f"Boat {boat.name} Imported with ID {boat.id}")

    existing_record = db.session.query(Boat).first()
    if existing_record is None:
        for boat_race in db.session.query(BoatRace).all():
            for i in range(random.randint(1, 10)):
                insert_record(boat_race)
