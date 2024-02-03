import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate


class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
# Create a global Flask-Marshmallow object
ma = Marshmallow()
migrate = Migrate()

def create_app(test_config=None):
    # create the Flask app
    app = Flask(__name__, instance_relative_config=True)
    # configure the Flask app (see later notes on how to generate your own SECRET_KEY)
    app.config.from_mapping(
        SECRET_KEY='jvLgWzRRFHcnNE8u2ClbMQ',
        # Set the location of the database file called paralympics.sqlite which will be in the app's instance folder
        SQLALCHEMY_DATABASE_URI= "sqlite:///" + os.path.join(app.instance_path, 'data.sqlite'),  
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
# Initialise Flask with the SQLAlchemy database extension
    db.init_app(app)
    migrate.init_app(app, db)

 # Initialise Flask-Marshmallow
    ma.init_app(app)

    # Create the tables in the database and register the routes
    with app.app_context():
        # Models are defined in the models module
        from src.models import User, Case, Complaint, Dashboard, Filter
        db.create_all()
        # Add the data to the database if not already added
        add_data_from_csv()

 # Register the routes from paralympics.py with the app

        from src import routes # Import routes from the routes module
    return app



def add_data_from_csv():
    import csv
    from pathlib import Path

    # Import models here to avoid circular import issues
    from src.models import Case, Complaint, Dashboard

    dataset_file = Path(__file__).parent.joinpath("data", "dataset_prepared.csv")

    with open(dataset_file, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip header row
        # Add Case data
        first_case = db.session.query(Case).first()
        if not first_case:
            for row in csv_reader:
                case = Case(
                    case_type=row[0],
                    status=row[1],
                    request_received_year=row[2],
                    request_received_month=row[3],
                    request_closed_year=row[4],
                    request_closed_month=row[5],
                    # ... other fields as per your Case model
                )
                db.session.add(case)
            db.session.commit()  # Commit after adding all cases

        # Add Complaint data
        first_complaint = db.session.query(Complaint).first()
        if not first_complaint:
            for row in csv_reader:
                # Assuming complaint data follows case data in the CSV
                complaint = Complaint(reason_grouped=row[9])
                db.session.add(complaint)
            db.session.commit()  # Commit after adding all complaints

        # Add Dashboard data
        first_dashboard = db.session.query(Dashboard).first()
        if not first_dashboard:
            for row in csv_reader:
                # Assuming dashboard data follows complaint data in the CSV
                dashboard = Dashboard(
                    active_days=row[6],
                    closed_on_time=row[8],
                    case_active_grouped=row[7]
                )
                db.session.add(dashboard)
            db.session.commit()  # Commit after adding all dashboards


