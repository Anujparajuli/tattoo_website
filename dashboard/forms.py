from django import forms
from .models import Booking
from .models import ContactMessage

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'email', 'phone', 'artist', 'placement', 'description', 'reference', 'date']





class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']

