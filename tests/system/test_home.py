from unittest import TestCase
#base class for writing test cases
from app import app
import json

class TestHome(TestCase):
    #TestHome inherits from TestCase
    def test_home(self):
        #creating a test client object from the Flask app
        #the test client allows us to simulate requests to the Flask app during testing
        with app.test_client() as c:
            #sending a GET request to the root URL
            response = c.get('/')

            #asserting that the status code of the response is
            #=200, which indicates a successful HTTP response
            self.assertEqual(response.status_code, 200)

            #asserting that the response data parsed as JSON
            #using json.loads is equal to my dict
            self.assertEqual(json.loads(response.get_data()),
                             {'message':"Hello, world!"})
