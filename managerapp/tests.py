from .models import Customer,Seat
from django.test import TestCase
import requests, json
from managerapp.testfunctions import *
BASE_URL = 'http://127.0.0.1:8000/'



class BookSeatTest(TestCase,OccupyTestFuctions):
    """Test class for seat reservaiton"""

    def test_create_valid_reservation(self):
        # Providing credentials correctly
        response = self.create_valid_resource()
        self.assertEqual(response.status_code, 200)

    def test_create_invalid_reservation(self):
        # Providing invalid information which is not present
        response = self.create_invalid_resource()
        self.assertEqual(response.status_code, 404)

class VacateTest(TestCase, VacateTestFuctions):
    """Test class for vacating seat""" 
    def test_create_valid_vacate(self):
        # Passing valid seat_no
        response = self.delete_resource(4)
        self.assertEqual(response.status_code, 200)
 
    def test_create_invalid_vacate(self):
        # Vacating the seat which is not allotted.
        response = self.delete_resource(51)
        self.assertEqual(response.status_code, 404)
