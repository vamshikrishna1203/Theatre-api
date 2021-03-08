from managerapp.models import Seat,Customer
from django.conf import settings
from django.http import HttpResponse

class HttpResponseMixin(object):

    def render_to_http_response(self, json_data, status = 200):
        return HttpResponse(json_data, content_type = 'application/json', status= status)

class RetriveMixin(object):


    def get_data(self,seat):
        data = {
            'name': seat.customer.u_name,
            'ticket': str(seat.customer.ticket_id),
            'seat_no': seat.seat_no
        }
        return data

    def get_object_by_seat(self,seat_no):
        con = Seat.objects.get(seat_no = seat_no)
        return self.get_data(con)

    def get_object_by_ticket(self,ticket_id):
        lis = []
        con = Seat.objects.all()
        for i in con:
            if str(i.customer.ticket_id) == ticket_id:
                lis.append(self.get_data(i))
        return lis

    def get_object_by_name(self,u_name):
        lis= []
        con = Seat.objects.all()
        for i in con:
            if i.customer.u_name == u_name:
                lis.append(self.get_data(i))
        return lis