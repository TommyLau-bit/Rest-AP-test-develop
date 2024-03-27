import requests
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import pytest



@pytest.mark.parametrize("page_url, expected_title", [
    ("/", "Home"),
    ("/list_complaints", "Complaints"),
    ("/show_dashboard", "Dashboard"),
    ("/list_cases", "List of Cases"),
    ("/user_profile", "User Profile"),
    ("/add_form", "Add New Form")
])

def test_server_is_up_and_running(live_server_flask, flask_port):
    """
    GIVEN a live server
    WHEN a GET HTTP request to the home page is made
    THEN the HTTP response should have a bytes string "User", "Case", and "Complaint" in the data and a status code of 200
    """
    url = f'http://127.0.0.1:{flask_port}/'
    response = requests.get(url)
    assert response.status_code == 200
    assert b"User" in response.content
    assert b"Case" in response.content
    assert b"Complaint" in response.content

def test_home_page_title(chrome_driver, live_server_flask, flask_port):
    """
    GIVEN a running app
    WHEN the homepage is accessed
    THEN the value of the page title should be "MyApp - Home"
    """
    url = f'http://127.0.0.1:{flask_port}/'
    chrome_driver.get(url)
    # Wait for the title to be there and its value to be "MyApp - Home", times out after 2 seconds
    WebDriverWait(chrome_driver, 2).until(EC.title_is("MyApp - Home"))
    assert chrome_driver.title == "MyApp - Home"


def test_page_titles(chrome_driver, live_server_flask, flask_port, page_url, expected_title):
    url = f'http://127.0.0.1:{flask_port}{page_url}'
    chrome_driver.get(url)
    WebDriverWait(chrome_driver, 5).until(EC.title_contains(expected_title))
    assert chrome_driver.title == f"MyApp - {expected_title}"


def test_navigation_links(chrome_driver, live_server_flask, flask_port):
    # Test navigation links in navbar
    url = f'http://127.0.0.1:{flask_port}/'
    chrome_driver.get(url)

    # Find and click on each navigation link
    nav_links = chrome_driver.find_elements_by_css_selector('.navbar-nav .nav-link')
    for link in nav_links:
        link_text = link.text
        link.click()
        WebDriverWait(chrome_driver, 5).until(EC.title_contains(link_text))
        assert link_text in chrome_driver.title

def test_add_form_page(chrome_driver, live_server_flask, flask_port):
    # Test if add form page loads and form fields are present
    url = f'http://127.0.0.1:{flask_port}/add_form'
    chrome_driver.get(url)

    # Assuming form fields are present
    form_fields = ['case_type', 'status', 'request_received_year', 'request_received_month',
                   'request_closed_year', 'request_closed_month', 'reason_grouped',
                   'active_days', 'closed_on_time', 'case_active_grouped', 'criteria']
    for field in form_fields:
        assert chrome_driver.find_element_by_name(field)

def test_chart_page(chrome_driver, live_server_flask, flask_port):
    # Test if chart page loads and contains chart elements
    url = f'http://127.0.0.1:{flask_port}/chart'
    chrome_driver.get(url)

    # Assuming chart elements are present
    assert chrome_driver.find_element_by_tag_name('h2').text == 'Dashboard Chart'
    assert chrome_driver.find_element_by_id('dashboard_chart').is_displayed()

def test_list_cases_page(chrome_driver, live_server_flask, flask_port):
    # Test if list cases page loads and displays cases correctly
    url = f'http://127.0.0.1:{flask_port}/list_cases'
    chrome_driver.get(url)

    # Assuming cases are displayed in a table
    assert chrome_driver.find_element_by_tag_name('h2').text == 'All Cases'
    assert chrome_driver.find_element_by_tag_name('table')

def test_user_profile_page(chrome_driver, live_server_flask, flask_port):
    # Test if user profile page loads and displays user information correctly
    url = f'http://127.0.0.1:{flask_port}/user_profile'
    chrome_driver.get(url)

    # Assuming user profile information is displayed correctly
    assert chrome_driver.find_element_by_tag_name('h2').text == 'User Profile'
    assert chrome_driver.find_element_by_tag_name('p').text.startswith('Email:')
    assert chrome_driver.find_element_by_tag_name('h3').text == 'Associated Cases:'
    assert chrome_driver.find_element_by_tag_name('h3').text == 'Filed Complaints:'
    # Add assertions to check user profile information as needed

def test_case_detail_page(chrome_driver, live_server_flask, flask_port):
    # Test if case detail page loads and displays case details correctly
    url = f'http://127.0.0.1:{flask_port}/case_detail'
    chrome_driver.get(url)

    # Assuming case details are displayed correctly
    assert chrome_driver.find_element_by_tag_name('h2').text == 'Case Details'
    assert chrome_driver.find_element_by_tag_name('h5').text.startswith('Case ID:')
    assert chrome_driver.find_element_by_tag_name('p').text.startswith('Type:')
    assert chrome_driver.find_element_by_tag_name('p').text.startswith('Status:')
    # Add assertions to check case details as needed

def test_list_complaints_page(chrome_driver, live_server_flask, flask_port):
    # Test if list complaints page loads and displays complaints correctly
    url = f'http://127.0.0.1:{flask_port}/list_complaints'
    chrome_driver.get(url)

    # Assuming complaints are displayed in a table
    assert chrome_driver.find_element_by_tag_name('h2').text == 'All Complaints'
    assert chrome_driver.find_element_by_tag_name('table')
    # Add assertions to check complaints list as needed