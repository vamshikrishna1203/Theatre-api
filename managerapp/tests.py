from .models import Customer,Seat
from django.test import TestCase
import requests, json
BASE_URL = 'http://127.0.0.1:8000/'

class BookSeatTest(TestCase):
    """ Test module for seat reservaiton """


    def setUp(self):
        self.valid_payload = {
            'name': 'vamshi',
            'ticket_id': '2e6e79c4-aa80-406a-9517-9b75552eb7ed',
        }
        self.invalid_payload = {
            'name': 'vamshi',
            'ticket_id': 'ee7a65a9-6f7f-43cb-8cff-1b4f43350e7e',
        }



    def test_create_valid_reservation(self):
        response = requests.post( BASE_URL +'occupy/', data = json.dumps(self.valid_payload) )
        self.assertEqual(response.status_code, 200)
        print(response.json())

    def test_create_invalid_reservation(self):
        response = requests.post( BASE_URL +'occupy/', data = json.dumps(self.invalid_payload) )
        self.assertEqual(response.status_code, 500)