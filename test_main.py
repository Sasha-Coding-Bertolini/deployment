from main import app  # Import your Flask app from the main app file

# A basic test for the root route '/'
def test_index_route():
    client = app.test_client()  # Create a test client
    response = client.get('/')  # Send a GET request to the '/' route
    assert response.status_code == 200  # Check if the response status code is 200

# Another basic test for the '/cow' route
def test_cow_route():
    client = app.test_client()
    response = client.get('/cow')
    assert response.status_code == 200

