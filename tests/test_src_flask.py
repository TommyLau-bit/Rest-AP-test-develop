import requests
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


def test_server_running(live_server):
    """Test that the server is running."""
    url = live_server
    response = requests.get(url)
    assert response.status_code == 200, f"Failed to access server at {url}. Status code: {response.status_code}"

def test_element_value(chrome_driver, live_server):
    """Test the value of an element on the page."""
    chrome_driver.get(live_server)
    element = chrome_driver.find_element(By.ID, "recent-cases-heading")
    element.click()
    highlights_element = chrome_driver.find_element(By.ID, "dashboard-metrics-heading")
    highlights_value = highlights_element.text
    assert highlights_value == "Dashboard Metrics"

def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Recent Cases" in response.data
    assert b"Recent Complaints" in response.data
    assert b"Dashboard Metrics" in response.data


def test_case_detail(client):
    # Assuming there's a case with ID=2 in your database
    response = client.get('/case/2')
    assert response.status_code == 200
    assert b"Case Details" in response.data
    assert b"Type:" in response.data
    assert b"Status:" in response.data

def test_list_cases(client):
    response = client.get('/cases')
    assert response.status_code == 200
    assert b"FOIA Case" in response.data




