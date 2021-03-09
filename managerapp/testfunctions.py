import requests
import json
BASE_URL = 'http://127.0.0.1:8000/'


class GetInfoTestFucntion:
    def get_resource(self, data):
        # TestCase for  /get_info/<NAME or SEATNUM or TICKETID>
        # Takes SEATNUM or TICKETID or NAME
        response = requests.get(BASE_URL + 'get_info/' + str(data) + '/')
        return response


class OccupyTestFuctions:
    def create_valid_resource(self, name, ticket_id):
        # TestCase for /occupy/
        # Formating data according to Consumer object present in model objects
        data = {
            'name': name,
            'ticket_id': ticket_id
        }
        response = requests.post(BASE_URL + 'occupy/', data=json.dumps(data))
        return response

    def create_invalid_resource(self, name, ticket_id):
        # TestCase for /occupy/
        # Formating data according to Consumer object present in model objects
        data = {
            'name': name,
            'ticket_id': ticket_id
        }
        response = requests.post(BASE_URL + 'occupy/', data=json.dumps(data))
        return response


class VacateTestFuctions:
    def delete_resource(self, id):
        # TestCase for /vacate/
        response = requests.delete(BASE_URL + 'vacate/' + str(id) + '/')
        return response
