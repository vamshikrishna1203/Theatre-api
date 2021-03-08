from consumer_app.models import Seat,Customer
from django.conf import settings
from django.http import HttpResponse
class RetriveMixin(object):


    def get_data(self,seat):
        data = {
            'name': seat.consumer.u_name,
            'ticket': str(seat.consumer.ticket_id),
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