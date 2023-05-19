from unittest import TestCase
from app import app

class TestAbout(TestCase):
    def test_about_route(self):
        with app.test_client() as c:
            response = c.get('/about')

            self.assertEqual(response.status_code, 200)


    def test_about_template_render(self):
        with app.test_client() as c:
            #sending a GET request to the /about route of app through test client
            #and storing the response received from the server in the response variable
            response = c.get('/about')

            #assigning to a variable what we want to verify and compare to the actual response
            #b' - string should be treated as a sequence of bytes
            #byte strings
            #response.data returns the content of the response as bytes
            expected_heading = b'<h1>About Routing and View Functions</h1>'

            #extracting the content of the response received from the server
            #assigning the actual data of the response
            rendered_template = response.data

            #verify that the data in expected_heading is contained within the actual data
            #from the rendered_template
            self.assertIn(expected_heading,rendered_template)