from app import app

def test_home_returns_200():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    
    """ Note - 
    this is test cases created to test the python application and the details as mentioned below:
    
    client -> used here is browser 
    response -> localhost:8085/ and this should return 200 status code if application is running 
    fine 
    
    For this need to install pytest -> requirement.txt
    """