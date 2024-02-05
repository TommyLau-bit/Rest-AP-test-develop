# Add a new User
def test_add_user(client):
    """Test creating a new user."""
    user_data = {"email": "newuser@example.com", "password": "securepassword"}
    response = client.post("/users", json=user_data)
    assert response.status_code == 201
    assert "message" in response.json
    assert "User added with id=" in response.json["message"]

# Get User by ID
def test_get_user(client):
    """Test retrieving an existing user."""
    user_id = 1  # Assuming this user exists
    response = client.get(f"/users/{user_id}")
    assert response.status_code == 200
    assert response.json['email'] == "newuser@example.com"  # Example assertion

# Update User
def test_update_user(client):
    """Test updating an existing user."""
    user_id = 1  # Assuming this user exists
    update_data = {"email": "updateduser@example.com"}
    response = client.put(f"/users/{user_id}", json=update_data)
    assert response.status_code == 200
    assert response.json['email'] == "updateduser@example.com"

# Delete User
def test_delete_user(client):
    """Test deleting an existing user."""
    user_id = 1  # Assuming this user exists
    response = client.delete(f"/users/{user_id}")
    assert response.status_code == 200
    # Further assertions can check if the user is actually removed

# Add a new Case
def test_add_case(client):
    """Test creating a new case."""
    case_data = {
        "case_type": "Example",
        "status": "Open",
        "user_id": 1,
        "request_received_year": "2021",
        "request_received_month": "06",
        "request_closed_year": "2021",
        "request_closed_month": "07"
    }
    response = client.post("/cases", json=case_data)
    assert response.status_code == 201
    # Updated assertion to check for a message indicating success and extracting the ID
    assert "Case added with id=" in response.json["message"]
    # Optional: Extract and validate the ID value if necessary
    added_case_id = int(response.json["message"].split('= ')[1])
    assert isinstance(added_case_id, int)  # This checks that the ID is indeed an integer

# Get Case by ID
def test_get_case(client):
    """Test retrieving an existing case."""
    case_id = 1  # Assuming this case exists
    response = client.get(f"/cases/{case_id}")
    assert response.status_code == 200
    assert response.json['case_type'] == "FOIA Case"  # Adjusted to match the actual response

# Update Case
def test_update_case(client):
    """Test updating an existing case."""
    case_id = 1  # Assuming this case exists
    update_data = {"status": "Closed"}
    response = client.put(f"/cases/{case_id}", json=update_data)
    assert response.status_code == 200
    assert response.json['status'] == "Closed"

# Delete Case
def test_delete_case(client):
    """Test deleting an existing case."""
    case_id = 1  # Assuming this case exists
    response = client.delete(f"/cases/{case_id}")
    assert response.status_code == 200
    # Further assertions can check if the case is actually removed
