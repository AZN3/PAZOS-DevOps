from django.test import TestCase

# Create your tests here.
from django.test import Client

class SimpleTest(TestCase):
    def setUp(self):

        self.client = Client()

    def test_details(self):
        # GET requests.
        response_hasher = self.client.get('/hasher/your_hash')
        response_IP = self.client.get('/ip_checker/your_IP')

        # checking if the responses are with the 202 OK HTTP code with the GET method, even the post method is required
        self.assertEqual(response_hasher.status_code,200)
        self.assertEqual(response_IP.status_code,200)