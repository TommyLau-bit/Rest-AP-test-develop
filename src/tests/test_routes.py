def test_get_users_status_code(client):
    """
    GIVEN a Flask test client
    WHEN a request is made to /users
    THEN the status code should be 200
    """
    response = client.get("/users")
    assert response.status_code == 200

def test_get_users_json(client):
    """
    GIVEN a Flask test client
    AND the database contains user data
    WHEN a request is made to /users
    THEN the response should contain JSON
    AND a JSON object for a user should be in the JSON
    """
    response = client.get("/users")
    assert response.headers["Content-Type"] == "application/json"
    
    user_data = {
        "email": "testuser@example.com",
        "password": "testpassword",
        # Add other user attributes here
    }
    
    assert user_data in response.json

def test_get_cases_status_code(client):
    """
    GIVEN a Flask test client
    WHEN a request is made to /cases
    THEN the status code should be 200
    """
    response = client.get("/cases")
    assert response.status_code == 200

def test_get_cases_json(client):
    """
    GIVEN a Flask test client
    AND the database contains case data
    WHEN a request is made to /cases
    THEN the response should contain JSON
    AND a JSON object for a case should be in the JSON
    """
    response = client.get("/cases")
    assert response.headers["Content-Type"] == "application/json"
    
    case_data = {
        "case_type": "Test Case",
        "status": "Open",
        # Add other case attributes here
    }
    
    assert case_data in response.json


# Add similar test functions for other routes related to filters

def test_get_users(client):
    """
    GIVEN a Flask test client
    WHEN a request is made to /users
    THEN the response status code should be 200
    AND the response should contain JSON data for all users
    """
    response = client.get("/users")
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    # You can add more specific assertions to check the JSON data

def test_get_user(client):
    """
    GIVEN a Flask test client
    WHEN a request is made to /users/<user_id>
    THEN the response status code should be 200 if the user exists
    AND the response should contain JSON data for the specified user
    """
    user_id = 1  
    response = client.get(f"/users/{user_id}")
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    # You can add more specific assertions to check the JSON data

def test_get_user_not_found(client):
    """
    GIVEN a Flask test client
    WHEN a request is made to /users/<non_existent_user_id>
    THEN the response status code should be 404 Not Found
    """
    non_existent_user_id = 99999  
    response = client.get(f"/users/{non_existent_user_id}")
    assert response.status_code == 404

# Similar tests can be created for other models (e.g., Case, Complaint, Dashboard, Filter)

def test_get_cases(client):
    """
    GIVEN a Flask test client
    WHEN a request is made to /cases
    THEN the response status code should be 200
    AND the response should contain JSON data for all cases
    """
    response = client.get("/cases")
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    # You can add more specific assertions to check the JSON data

def test_get_case(client):
    """
    GIVEN a Flask test client
    WHEN a request is made to /cases/<case_id>
    THEN the response status code should be 200 if the case exists
    AND the response should contain JSON data for the specified case
    """
    case_id = 1  
    response = client.get(f"/cases/{case_id}")
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    # You can add more specific assertions to check the JSON data

def test_get_case_not_found(client):
    """
    GIVEN a Flask test client
    WHEN a request is made to /cases/<non_existent_case_id>
    THEN the response status code should be 404 Not Found
    """
    non_existent_case_id = 999999 # Replace with a non-existent case ID
    response = client.get(f"/cases/{non_existent_case_id}")
    assert response.status_code == 404


def test_post_complaint(client):
    """
    GIVEN a Flask test client
    AND valid JSON for a new complaint
    WHEN a POST request is made to /complaints
    THEN the response status_code should be 201
    """
    # JSON to create a new complaint
    complaint_json = {
        "reason_grouped": "Service Issue",
        "user_id": 1  
    }
    # pass the JSON in the HTTP POST request
    response = client.post(
        "/complaints",
        json=complaint_json,
        content_type="application/json",
    )
    # 201 is the HTTP status code for a successful POST or PUT request
    assert response.status_code == 201

def test_complaint_post_error(client):
    """
    GIVEN a Flask test client
    AND JSON for a new complaint that is missing a required field ("reason_grouped")
    WHEN a POST request is made to /complaints
    THEN the response status_code should be 400
    """
    missing_reason_json = {"user_id": 1}  
    response = client.post("/complaints", json=missing_reason_json)
    assert response.status_code == 400

def test_post_dashboard(client, db_session):
    """
    GIVEN a Flask test client
    AND valid JSON for a new dashboard
    WHEN a POST request is made to /dashboards
    THEN the response status_code should be 201
    """
    # Create a Dashboard JSON with real data
    dashboard_json = {
        "active_days": "10",
        "closed_on_time": "Yes",
        "case_active_grouped": "Grouped",
        "user_id": 1
    }

    # Use SQLAlchemy to add the dashboard to the database
    response = client.post(
        "/dashboards",
        json=dashboard_json,
        content_type="application/json",
    )
    # Assert that the dashboard was added successfully
    assert response.status_code == 201

    # Optionally, you can query the database to verify the data was added correctly

def test_dashboard_post_error(client):
    """
    GIVEN a Flask test client
    AND JSON for a new dashboard that is missing a required field ("active_days")
    WHEN a POST request is made to /dashboards
    THEN the response status_code should be 400
    """
    # Create a Dashboard JSON with a missing required field
    missing_active_days_json = {
        "closed_on_time": "Yes",
        "case_active_grouped": "Grouped",
        "user_id": 1
    }
    response = client.post("/dashboards", json=missing_active_days_json)
    assert response.status_code == 400

def test_patch_complaint(client, db_session):
    """
    GIVEN an existing complaint
    AND a Flask test client
    WHEN a PATCH request is made to /complaints/<complaint_id> with updated data
    THEN the response status_code should be 200
    AND the response content should include the message 'Complaint <complaint_id> updated'
    """
    complaint_id = 1
    updated_complaint_data = {
        "reason_grouped": "Updated Reason",
        "user_id": 1
    }

    response = client.patch(f"/complaints/{complaint_id}", json=updated_complaint_data)
    assert response.json['message'] == f'Complaint {complaint_id} updated.'
    assert response.status_code == 200

def test_complaint_patch_error(client):
    """
    GIVEN a Flask test client
    AND a PATCH request is made to /complaints/<complaint_id> with invalid data
    THEN the response status_code should be 400
    """
    complaint_id = 1
    invalid_complaint_data = {
        # Missing required field "reason_grouped"
        "user_id": 1
    }

    response = client.patch(f"/complaints/{complaint_id}", json=invalid_complaint_data)
    assert response.status_code == 400

def test_patch_dashboard(client, db_session):
    """
    GIVEN an existing dashboard
    AND a Flask test client
    WHEN a PATCH request is made to /dashboards/<dashboard_id> with updated data
    THEN the response status_code should be 200
    AND the response content should include the message 'Dashboard <dashboard_id> updated'
    """
    dashboard_id = 1
    updated_dashboard_data = {
        "active_days": "Updated Days",
        "closed_on_time": "No",
        "case_active_grouped": "Updated Group",
        "user_id": 1
    }

    response = client.patch(f"/dashboards/{dashboard_id}", json=updated_dashboard_data)
    assert response.json['message'] == f'Dashboard {dashboard_id} updated.'
    assert response.status_code == 200

def test_dashboard_patch_error(client):
    """
    GIVEN a Flask test client
    AND a PATCH request is made to /dashboards/<dashboard_id> with invalid data
    THEN the response status_code should be 400
    """
    dashboard_id = 1
    invalid_dashboard_data = {
        # Missing required field "active_days"
        "closed_on_time": "No",
        "case_active_grouped": "Updated Group",
        "user_id": 1
    }

    response = client.patch(f"/dashboards/{dashboard_id}", json=invalid_dashboard_data)
    assert response.status_code == 400

def test_delete_complaint(client, db_session):
    """
    GIVEN an existing complaint
    AND a Flask test client
    WHEN a DELETE request is made to /complaints/<complaint_id>
    THEN the response status code should be 200
    AND the response content should include the message 'Complaint {complaint_id} deleted.'
    """
    complaint_id = 1

    response = client.delete(f"/complaints/{complaint_id}")
    assert response.status_code == 200
    assert response.json['message'] == f'Complaint {complaint_id} deleted.'

def test_delete_complaint_not_found(client):
    """
    GIVEN a Flask test client
    AND a DELETE request is made to /complaints/<complaint_id> for a non-existent complaint
    THEN the response status code should be 404
    """
    # Assuming you have a non-existent complaint ID (e.g., 99999) in your database
    non_existent_complaint_id = 99999

    response = client.delete(f"/complaints/{non_existent_complaint_id}")
    assert response.status_code == 404

def test_delete_dashboard(client, db_session):
    """
    GIVEN an existing dashboard
    AND a Flask test client
    WHEN a DELETE request is made to /dashboards/<dashboard_id>
    THEN the response status code should be 200
    AND the response content should include the message 'Dashboard {dashboard_id} deleted.'
    """
    dashboard_id = 1

    response = client.delete(f"/dashboards/{dashboard_id}")
    assert response.status_code == 200
    assert response.json['message'] == f'Dashboard {dashboard_id} deleted.'

def test_delete_dashboard_not_found(client):
    """
    GIVEN a Flask test client
    AND a DELETE request is made to /dashboards/<dashboard_id> for a non-existent dashboard
    THEN the response status code should be 404
    """
    # Assuming you have a non-existent dashboard ID (e.g., 99999) in your database
    non_existent_dashboard_id = 99999

    response = client.delete(f"/dashboards/{non_existent_dashboard_id}")
    assert response.status_code == 404
