from unittest import TestCase
from app import app

class TestAbout(TestCase):
    def test_about_route(self):
        with app.test_client() as c:
            response = c.get('/about')

            self.assertEqual(response.status_code, 200)


    def test_about_template_render(self):
        with app.test_client() as c:
            response = c.get('/about')
            expected_heading= b'<h1>About Routing and View Functions</h1>'
            rendered_template = response.data

            self.assertIn(expected_heading,rendered_template)