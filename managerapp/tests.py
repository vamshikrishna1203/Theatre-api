from .models import Customer,Seat
from django.test import TestCase
import requests, json
from managerapp.testfunctions import *
BASE_URL = 'http://127.0.0.1:8000/'



class BookSeatTest(TestCase,OccupyTestFuctions):
    """Test class for seat reservaiton"""

    def test_create_valid_reservation(self):
        # Providing credentials correctly
        # Provide values of objects in currnet model
        valid_name = 'vamshi'
        valid_ticket = '2e6e79c4-aa80-406a-9517-9b75552eb7ed'
        response = self.create_valid_resource(valid_name,valid_ticket)
        self.assertEqual(response.status_code, 200)

    def test_create_invalid_reservation(self):
        # Providing invalid information which is not present
        invalid_name = 'hari'
        valid_ticket = '2e6e79c4-aa80-406a-9517-9b75552eb7ed'
        response = self.create_invalid_resource(invalid_name, valid_ticket)
        self.assertEqual(response.status_code, 404)
        
class GetPersonTest(TestCase, GetInfoTestFucntion):
    def get_valid_person_by_name(self):
        name = 'vamshi'
        response = self.get_resource(name)
        self.assertEqual(response.status_code, 200)

    def get_valid_person_by_ticket(self):
        ticket_id = '2e6e79c4-aa80-406a-9517-9b75552eb7ed'
        response = self.get_resource(ticket_id)
        self.assertEqual(response.status_code, 200)   

    def get_valid_person_by_seat(self):
        seat_no = 1
        response = self.get_resource(seat_no)
        self.assertEqual(response.status_code, 200)   

class VacateTest(TestCase, VacateTestFuctions):
    """Test class for vacating seat""" 
    def test_create_valid_vacate(self):
        # Passing valid seat_no
        # vacating seat_no present in model
        response = self.delete_resource(4)
        self.assertEqual(response.status_code, 200)
 
    def test_create_invalid_vacate(self):
        # Vacating the seat which is not allotted.
        # vacating seat_no not allocated
        response = self.delete_resource(51)
        self.assertEqual(response.status_code, 404)
