# tests/test_db_read.py
import unittest
from pymongo import MongoClient
from dotenv import load_dotenv
import os
 
load_dotenv()
mongo_uri = os.getenv('MONGODB_URI')
 
class TestDatabaseRead(unittest.TestCase):
    def setUp(self):
        # Connect to MongoDB (ensure your .env file is loaded for credentials)
        self.client = MongoClient(mongo_uri)
        self.db = self.client['shop_db']
 
    def test_ping_db(self):
        """Test the MongoDB connection using ping."""
        response = self.client.admin.command('ping')
        self.assertEqual(response['ok'], 1.0)
 
if __name__ == '__main__':
    unittest.main()
 
 