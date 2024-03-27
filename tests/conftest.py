import os
import pytest
from src import create_app
from src.models import db
from pathlib import Path
from selenium.webdriver import Chrome, ChromeOptions
import socket
import subprocess
import time

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




@pytest.fixture(scope="module")
def chrome_driver():
    """
    Fixture to create a Chrome driver. 
    
    On GitHub or other container it needs to run headless, i.e. the browser doesn't open and display on screen.
    Running locally you may want to display the tests in a large window to visibly check the behaviour. 
    """
    options = ChromeOptions()
    if "GITHUB_ACTIONS" in os.environ:
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--headless")
    else:
        options.add_argument("start-maximized")
    driver = Chrome(options=options)
    yield driver
    driver.quit()
    

@pytest.fixture(scope="session")
def flask_port():
    """Gets a free port from the operating system."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("", 0))
        addr = s.getsockname()
        port = addr[1]
        return port


@pytest.fixture(scope="session")
def live_server_flask(flask_port):
    """Runs the Flask app as a live server for Selenium tests"""

    app_command = f"flask --app '{create_app}:create_app(test_config={'TESTING': True, 'WTF_CSRF_ENABLED': False})' run --port {flask_port}"

    try:
        server = subprocess.Popen(app_command, shell=True)
        # Allow time for the app to start
        time.sleep(3)
        yield server
        server.terminate()
    except subprocess.CalledProcessError as e:
        print(f"Error starting Flask app: {e}")


@pytest.fixture(scope="session")
def app():
    """Fixture to create the src_flask app and configure it for testing

    Required by the pytest-flask library; must be called 'app'
    """
    test_cfg = {
        "TESTING": True,
        "WTF_CSRF_ENABLED": False
    }
    app = create_app(test_config=test_cfg)
    yield app
