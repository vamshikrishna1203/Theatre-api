# mymangaer

## Overview

managerapp simple API manages the theatre occupancy. The theatre is a new Arena theatre for live performances and does not assign fixed seating number assignments to its patrons .

## Assumptions

```    
    1. Each person is uniquely identified by ticket_id.
    2. Once a person is deleted, seats associated with the person will be vacated.
    3. Using one ticket_id person can occupy any number of seats.

```

## Open Endpoints

```
Open endpoints require no Authentication.
    • Occupy Seat: POST /occupy/
    • Vacate Seat: DELETE /vacate/<SEATNUM>
    • Get Person/Seat information: GET /get_info/<NAME or SEATNUM or TICKETID>/
```

## Built With
```
    • Python
    • Django
```

# Description
mytheatre is a website that uses managerapp api to gauge and manage theatre occupancy. API used here built with Python with Django. This is a RestApi request and responses are handled in JSON only.

The theatre is a new Arena theatre for live performances and does not assign fixed seating number assignments to its patrons. Since seats are dynamic and specified using max occupancy ticket_id doesn’t contain information of seat beforehand.


## Implementation Details:(managerapp)
Important implementation details of managerapp
### models.py:
```
    • Since ticket_id doesn’t contain information of seats beforehand two models are created.
    • Customer: contains two fields ticket_id(UUID, primary key), name(CharField).
    • Seat: contains two fields customer(Foreign Key Customer), seat(IntegerField, primary_key).
```

In order to book Seat, a person should be registered first. Each person(Customer) will be given a ticket_id which is unique. Seat can be booked once a person is registered.
On deleting person details(name, ticket_id) associated seat related to the person will be vacated.

### utils.py :
To implement utility functions. Example: To validate request and response headers.

### views.py:
Handles requests of URL endpoints and returns response.

### Classes Implemented:
```
    • class GetPerson(View, RetriveMixin, HttpResponseMixin):handles get request of /get_info/ url.
    • class Occupy(View, HttpResponseMixin, OccupyMixin):handles post request of /occupy/ url.
    • class Vacate(View, HttpResponseMixin):handles post request of /occupy/ url.
```

### mixins.py:
Mixin classes are parent classes that provide functionality to the child class but not to itself.
In this module, Mixins provides functionality to classes in views.py.

### Implemented mixins classes:
```
    • class HttpResponseMixin(object): Renders json to HttpResponse
    • class RetriveMixin(object):Retrieves information related objects on get request
    • class OccupyMixin(object):Allocates seat number for given data of customer on post request
```
### forms.py:
Contains modelForm classes used for post requests, creating objects, and validating
Post data.
### Classes Implemented:
```
    • class SeatForms(forms.ModelForm): Validates and create Seat Objects
```
### TestCases:
BASE_URL = 'http://127.0.0.1:8000/'
Basic test are included in mytheatre/mytheatre/test.py
#### 1.Occupy seat - [Endpoint URL - /occupy/ ] :
##### Invalid Scenarios:
```
    • Booking slot with invalid information.
    • Invalid ticket_id.
    • Booking slot when the capacity of the theatre is full.
 ```

##### Valid Scenarios:
```
    • Booking a slot with correct credentials.
```

#### 2.Vacate seat - [Endpoint URL - /vacate/ ]:
##### Invalid Scenarios:
```
    • Vacating the seat which is not allotted.
```
##### Valid Scenarios:
```
    • Passing valid seat_no.
```

#### 3.Get Person/Seat information - [Endpoint URL - /get_info/<NAME or SEATNUM or TICKETID> ]:
##### Invalid Scenarios:
```
    • Providing invalid information which is not present.
    • Providing invalid uuid format.
```
##### Valid Scenarios:
```
    • Providing credentials correctly.
```