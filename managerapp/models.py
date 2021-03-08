from django.db import models
import uuid

# Create your models here.
class Customer(models.Model):
    """
    Customer Model
    Defines the attributes of a customer
    """
    ticket_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length = 64)

class Seat(models.Model):
    """
    Seat Model
    Defines the attributes of a seat
    """
    consumer = models.ForeignKey(Customer,on_delete = models.CASCADE)
    seat_no = models.IntegerField(primary_key = True)