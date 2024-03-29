import pytest
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

@pytest.fixture
def client():
    with app.test_client() as client:
        with app.app_context():
            yield client

