from django import forms
from customer.models import Seat
from django.conf import settings
class SeatForms(forms.ModelForm):
    def clean_seat_no(self):
        inputseat = self.cleaned_data['seat_no']
        if inputseat > settings.MAX_CAPACITY:
            raise forms.ValidationError('Sorry slot is unavialble')
        return inputseat
    class Meta:
        model = Seat
        fields = '__all__'