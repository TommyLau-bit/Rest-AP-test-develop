import pytest
<<<<<<< HEAD
from selenium.webdriver import Chrome, ChromeOptions
from src import create_app
import subprocess
import time

@pytest.fixture(scope="module")
def app():
    """Create a Flask app instance for testing."""
    app = create_app()
    app.config["TESTING"] = True
    yield app

@pytest.fixture(scope="module")
def client(app):
    """Create a Flask test client."""
    return app.test_client()

@pytest.fixture(scope="module")
def chrome_driver():
    """Create a Chrome WebDriver for Selenium testing."""
    options = ChromeOptions()
    options.add_argument("--headless")  # Run Chrome in headless mode (no GUI)
    driver = Chrome(options=options)
    yield driver
    driver.quit()

@pytest.fixture(scope="session")
def live_server():
    """Create a live server instance for testing."""
    process = subprocess.Popen(["flask", "run", "--port", "5000"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    time.sleep(2)  # Allow some time for the server to start
    yield f"http://127.0.0.1:5000"
    process.terminate()  # Terminate the server process after testing
=======
from src import create_app
from src.models import db
from pathlib import Path

@pytest.fixture(scope='session') # the fixture is created once for the entire test session
def app():
    """Create and configure a new app instance for the test session."""
    db_path = Path(__file__).parent / 'data_testdb.sqlite'  # name of the test database is different from the main database
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
 
>>>>>>> 80d383b5124e4d5eab5e0f8fa6c3685fca041ae1
