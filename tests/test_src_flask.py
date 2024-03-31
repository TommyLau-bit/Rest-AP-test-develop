import requests
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


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

def test_search_functionality(chrome_driver, live_server):
    """Test the search functionality on the home page."""
    chrome_driver.get(live_server)
    search_input = chrome_driver.find_element(By.ID, "search-input")
    search_input.send_keys("FOIA Case")  # Searching for a specific case type
    search_input.send_keys(Keys.ENTER)
    
    # Wait for the search results to load
    WebDriverWait(chrome_driver, 10).until(
        EC.visibility_of_element_located((By.ID, "search-results"))
    )
    
    # Assuming the search results are displayed in a specific section of the page
    search_results_section = chrome_driver.find_element(By.ID, "search-results")
    assert "FOIA Case" in search_results_section.text

def test_navigation_to_case_detail(chrome_driver, live_server):
    """Test navigation to a case detail page from the home page."""
    chrome_driver.get(live_server)
    # Wait for the first 'View Case' link to be clickable
    WebDriverWait(chrome_driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".view-case-link"))  # Select by class
    )
    
    # Click the first 'View Case' link
    view_case_links = chrome_driver.find_elements(By.CSS_SELECTOR, ".view-case-link")
    if view_case_links:
        view_case_links[0].click()
    
    # Ensure the page has navigated to 'Case Details'
    WebDriverWait(chrome_driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "h2"))
    )
    assert "Case Details" in chrome_driver.page_source, "Failed to navigate to Case Details page."


