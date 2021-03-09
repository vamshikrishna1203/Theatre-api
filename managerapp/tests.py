from .models import Customer,Seat
from django.test import TestCase
import requests, json
from managerapp.testfunctions import *
BASE_URL = 'http://127.0.0.1:8000/'



class BookSeatTest(TestCase):
    """ Test module for seat reservaiton """

    def test_create_valid_reservation(self):
        response = create_valid_resource()
        self.assertEqual(response.status_code, 200)

    def test_create_invalid_reservation(self):
        response = create_invalid_resource()
        self.assertEqual(response.status_code, 404)

class VacateTest(TestCase):
    
    def test_create_valid_vacate(self):
        response = delete_resource(4)
        self.assertEqual(response.status_code, 200)

    def test_create_invalid_vacate(self):
        response = delete_resource(51)
        self.assertEqual(response.status_code, 404)
