import unittest   # Import the Flask app from app.py
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import app
 
class TestRoutes(unittest.TestCase):
    # Set up the Flask test client before each test
    def setUp(self):
        self.app = app.test_client()  # Create a test client for the Flask app
        self.app.testing = True  # Enable testing mode for the app
 
    # Test 1: Check if the home route returns a 200 status code
    def test_home_route(self):
        response = self.app.get('/')  # Simulate a GET request to the home route
        self.assertEqual(response.status_code, 200)  # Check if status code is 200
        self.assertIn(b'Welcome', response.data)  # Check if the response contains 'Welcome'
 
    # Test 2: Check if the /products route returns a 200 status code
    def test_products_route(self):
        response = self.app.get('/products')  # Simulate a GET request to the products route
        self.assertEqual(response.status_code, 200)  # Check if status code is 200
        self.assertIn(b'Products', response.data)  # Check if the response contains 'Products'
 
    # Test 3: Check if a POST request to the / route returns a 405 status code (Method Not Allowed)
    def test_home_route_post(self):
        response = self.app.post('/')  # Simulate a POST request to the home route
        self.assertEqual(response.status_code, 405)  # 405 means Method Not Allowed
 
if __name__ == '__main__':
    unittest.main()