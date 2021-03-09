from managerapp.models import Seat, Customer
from django.conf import settings
from django.http import HttpResponse
from django.forms import ValidationError

class HttpResponseMixin(object):
    """Renders json to HttpResponse"""

    def render_to_http_response(self, json_data, status=200):
        """Inputs json_data returns HttpResponse"""
        return HttpResponse(json_data, content_type='application/json',
                            status=status)


class RetriveMixin(object):
    """Retrives information related objects on get request"""

    def get_data(self, seat):
        """ For given object
            returns dictionary to display informaiton on get request
            """
        data = {
            'name': seat.customer.name,
            'ticket': str(seat.customer.ticket_id),
            'seat_no': seat.seat_no
        }
        return data

    def get_object_by_seat(self, seat_no):
        """For given seat number of customer
           Returns Seat object associated
           """
        con = Seat.objects.get(seat_no=seat_no)
        return self.get_data(con)

    def get_object_by_ticket(self, ticket_id):
        """For given ticket id of customer
           Returns list of Seat object associated
           """
        lis = []
        con = Seat.objects.all()
        for i in con:
            if str(i.customer.ticket_id) == ticket_id:
                lis.append(self.get_data(i))
        return lis

    def get_object_by_name(self, name):
        """For given name of customer
           Returns list of Seat object associated
           """
        lis = []
        con = Seat.objects.all()
        for i in con:
            if i.customer.name == name:
                lis.append(self.get_data(i))
        return lis


class OccupyMixin(object):
    """Allocates seat number for given data of customer on post request"""

    def get_customer(self, data):
        """Validates customer data and returns associated object with data"""
        try:
            obj = Customer.objects.get(ticket_id=data['ticket_id'])
            if(obj.name == data['name']):
                return obj
        except ValidationError:
            return None

    def get_seat_no(self):
        """Returns seat number in serial order"""
        for seat_no in range(1, settings.MAX_CAPACITY + 1):
            if not Seat.objects.filter(seat_no=seat_no).exists():
                return seat_no
        return settings.MAX_CAPACITY + 1
