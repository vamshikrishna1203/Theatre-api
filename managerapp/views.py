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


"""Handles get request of /get_info/ url"""

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
                # RetriveMixin method mixins.py
                user = self.get_object_by_name(name)
            elif seat_no is not None:
                user = self.get_object_by_seat(seat_no)  # RetriveMixin method
            else:
                user = self.get_object_by_ticket(
                   ticket_id)  # RetriveMixin method
        except Seat.DoesNotExist:
            # Seat doesn't exist exception
            json_data = json.dumps({'msg': 'The requested resourse unavailable'})
            # HttpResponseMixin method mixins.py
            return self.render_to_http_response(json_data, status=404)

        if not user:
            # user not found exception
            json_data = json.dumps(
                {'msg': 'The requested resource unavailable'})
            return self.render_to_http_response(json_data, status=404)
        # gets person informaiton and returns json data
        json_data = json.dumps(user, indent=4)
        return self.render_to_http_response(json_data, status=200)

# Disable csrf token
@method_decorator(csrf_exempt, name='dispatch')
class Occpy(View, HttpResponseMixin, OccupyMixin):


"""Handles post request of /occupy/ url"""

  def post(self, request, *args, **kwargs):
       data = request.body
        # validating request data using is_json() utils.py
        valid_json = is_json(data)

        if not valid_json:
            # error message is returned if data is not json
            json_data = json.dumps({'msg': 'please send valid json data only'})
            return self.render_to_http_response(json_data, status=404)

        userdata = json.loads(data)
        # retriving customer object associated with data
        user = self.get_customer(userdata)  # OccupyMixin method mixins.py
        # If associated user is found Seat object is created
        if user is not None:
            seat_no = self.get_seat_no()  # OccupyMixin method mixins.py
            new_data = {
                'customer': user,
                'seat_no': seat_no

            }

        else:
            json_data = json.dumps(
                {'msg': 'please send valid data  or slots are not empty'})
            return self.render_to_http_response(json_data, status=404)

        # validates Seat data using form before Seat object creation
        form = SeatForms(new_data)  # forms.py
        if form.is_valid():
            form.save(commit=True)
            json_data = json.dumps({'msg': 'Resource Created Successfully'})
            return self.render_to_http_response(json_data, status=200)
        if form.errors:
            # returns error message when form is invalid
            json_data = json.dumps(form.errors['seat_no'])
            return self.render_to_http_response(json_data, status=500)


@method_decorator(csrf_exempt, name='dispatch')
class Vacate(View, HttpResponseMixin):
    """Handles post request of /occupy/ url"""

       def get_object_by_seat(self, seat_no):
            # retrive object by given seat_no
            try:
                seat = Seat.objects.get(seat_no=seat_no)
            except Seat.DoesNotExist:
                seat = None
            return seat

        def delete(self, request, seat_no, *args, **kwargs):
            seat = self.get_object_by_seat(seat_no)
            # If seat not present returns error message
            if seat is None:
                json_data = json.dumps(
                    {'msg': 'No matched record found cannot perform deletion'})
                return self.render_to_http_response(json_data, status=404)
            else:
                status, deleted_item = seat.delete()
                if status == 1:
                    # returns success message after successfull deletion of
                    # Seat object
                    json_data = json.dumps(
                        {'msg': 'performed deletion successfully'})
                    return self.render_to_http_response(json_data, status=200)

                # returns error message unable to delete
                json_data = json.dumps({'unable to delete plz try again'})
                return self.render_to_http_response(json_data, status=404)
