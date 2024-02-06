import pytest
from src import create_app
from src.models import db
from pathlib import Path

@pytest.fixture(scope='session') # the fixture is created once for the entire test session
def app():
    """Create and configure a new app instance for the test session."""
    db_path = Path(__file__).parent / 'data_testdb.sqlite'  # name of the test database is different from the production database
    test_config = {
        'TESTING': True,
        'SQLALCHEMY_DATABASE_URI': f'sqlite:///{db_path}'
    }
    
    app = create_app(test_config) # create the app with the test configuration

    with app.app_context():
        db.create_all()
    
    yield app

    with app.app_context():
        db.drop_all()

@pytest.fixture(scope='function') # the fixture is created once for each test function
def client(app):
    """A test client for the app."""
    return app.test_client()
 