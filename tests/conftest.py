import pytest
from src import create_app
from src.models import db
from pathlib import Path

@pytest.fixture(scope='session')
def app():
    """Create and configure a new app instance for the test session."""
    db_path = Path(__file__).parent / 'data_testdb.sqlite'  # Adjusted for the correct path
    test_config = {
        'TESTING': True,
        'SQLALCHEMY_DATABASE_URI': f'sqlite:///{db_path}'
    }
    
    app = create_app(test_config)

    with app.app_context():
        db.create_all()
    
    yield app

    with app.app_context():
        db.drop_all()

@pytest.fixture(scope='function')
def client(app):
    """A test client for the app."""
    return app.test_client()
