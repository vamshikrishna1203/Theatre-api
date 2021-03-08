from django.shortcuts import render
from managerapp.models import Seat,Customer
from managerapp.mixins import RetriveMixin, HttpResponseMixin, OccupyMixin
from django.views.generic import View
import json


from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from managerapp.utils import is_json


class GetPerson(View, RetriveMixin, HttpResponseMixin):

    def get(self,request,name=None,seat_no=None,ticket_id=None,*args, **kwargs):
        try:
            if name is not None: 
                user = self.get_object_by_name(name)
            elif seat_no is not None:
                user = self.get_object_by_seat(seat_no)
            else:
                user = self.get_object_by_ticket(ticket_id)
        except Seat.DoesNotExist:
            json_data = json.dumps({'msg':'The requested resourse unavailable'})
            return self.render_to_http_response(json_data,status= 404)

        if not user :
            json_data = json.dumps({'msg':'The requested resource unavailable'})
            return self.render_to_http_response(json_data,status= 404)
        json_data = json.dumps(user, indent= 4)
        return self.render_to_http_response(json_data,status= 200)


@method_decorator(csrf_exempt, name = 'dispatch')
class Occpy(View,HttpResponseMixin, OccupyMixin):       

    def post(self,request,*args, **kwargs):
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            json_data = json.dumps({'msg' : 'please send valid json data only'})
            return self.render_to_http_response(json_data,status= 404)

        userdata = json.loads(data)
        user = self.get_customer(userdata)


        if user is not None:
            seat_no = self.get_seat_no()
            new_data = {
                'customer' : user,
                'seat_no'  : seat_no

            }

        else:
            json_data = json.dumps({'msg':'please send valid data  or slots are not empty'})
            return self.render_to_http_response(json_data,status= 404)