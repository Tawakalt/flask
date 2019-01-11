import unittest
import json
from app.wsgi import app

class SampleTEst(unittest.TestCase):
    """ Testcase for the Authentication related API endpoints 
    """

    def setUp(self):

        # setup the app and push app context:
        self.app = app
        self.app_context = self.app.app_context()
        self.app_context.push()
        
        self.client = self.app.test_client()


    def test_sample_test(self, token=''):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)