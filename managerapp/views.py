from django.shortcuts import render
from managerapp.models import Seat, Customer
from managerapp.mixins import RetriveMixin, HttpResponseMixin, OccupyMixin
from django.views.generic import View
import json


from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from managerapp.utils import is_json
from managerapp.forms import SeatForms


class GetPerson(View, RetriveMixin, HttpResponseMixin):

    def get(
            self,
            request,
            name=None,
            seat_no=None,
            ticket_id=None,
            *args,
            **kwargs):
        try:
            if name is not None:
                user = self.get_object_by_name(name)
            elif seat_no is not None:
                user = self.get_object_by_seat(seat_no)
            else:
                user = self.get_object_by_ticket(ticket_id)
        except Seat.DoesNotExist:
            json_data = json.dumps(
                {'msg': 'The requested resourse unavailable'})
            return self.render_to_http_response(json_data, status=404)

        if not user:
            json_data = json.dumps(
                {'msg': 'The requested resource unavailable'})
            return self.render_to_http_response(json_data, status=404)
        json_data = json.dumps(user, indent=4)
        return self.render_to_http_response(json_data, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class Occpy(View, HttpResponseMixin, OccupyMixin):

    def post(self, request, *args, **kwargs):
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            json_data = json.dumps({'msg': 'please send valid json data only'})
            return self.render_to_http_response(json_data, status=404)

        userdata = json.loads(data)
        user = self.get_customer(userdata)

        if user is not None:
            seat_no = self.get_seat_no()
            new_data = {
                'customer': user,
                'seat_no': seat_no

            }

        else:
            json_data = json.dumps(
                {'msg': 'please send valid data  or slots are not empty'})
            return self.render_to_http_response(json_data, status=404)

        form = SeatForms(new_data)
        if form.is_valid():
            form.save(commit=True)
            json_data = json.dumps({'msg': 'Resource Created Successfully'})
            return self.render_to_http_response(json_data, status=200)
        if form.errors:
            json_data = json.dumps(form.errors['seat_no'])
            return self.render_to_http_response(json_data, status=500)


@method_decorator(csrf_exempt, name='dispatch')
class Vacate(View, HttpResponseMixin):
    def get_object_by_seat(self, seat_no):
        try:
            seat = Seat.objects.get(seat_no=seat_no)
        except Seat.DoesNotExist:
            seat = None
        return seat

    def delete(self, request, seat_no, *args, **kwargs):
        seat = self.get_object_by_seat(seat_no)
        if seat is None:
            json_data = json.dumps(
                {'msg': 'No matched record found cannot perform deletion'})
            return self.render_to_http_response(json_data, status=404)
        else:
            status, deleted_item = seat.delete()
            if status == 1:
                json_data = json.dumps(
                    {'msg': 'performed deletion successfully'})
                return self.render_to_http_response(json_data, status=200)

            json_data = json.dumps({'unable to delete plz try again'})
            return self.render_to_http_response(json_data, status=404)
