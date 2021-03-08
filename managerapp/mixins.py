from consumer_app.models import Seat,Consumer
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