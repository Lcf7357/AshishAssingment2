import unittest
from dotenv import load_dotenv
from pymongo import MongoClient
import os
 
load_dotenv()
mongo_uri = os.getenv('MONGODB_URI')
 
class TestDatabaseWrite(unittest.TestCase):
    def setUp(self):
        # Connect to MongoDB (ensure your .env file is loaded for credentials)
        self.client = MongoClient(mongo_uri)
        self.db = self.client['shop_db']
        self.collection = self.db['products']
 
    def test_insert_document(self):
        """Test inserting a document into the collection."""
        sample_product = {
            'name': 'Test Product',
            'tag': 'Test Category',
            'price': 10.99,
            'image_path': 'static/images/test_product.jpg'
        }
        result = self.collection.insert_one(sample_product)
        self.assertIsNotNone(result.inserted_id)
       
        # Clean up: remove the test document
        self.collection.delete_one({'_id': result.inserted_id})
 
if __name__ == '__main__':
    unittest.main()