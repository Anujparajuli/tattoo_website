from django import forms
from .models import Booking
from .models import ContactMessage

class BookingForm(forms.ModelForm):
    # Make phone required
    phone = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your phone number'})
    )

    # Make description optional
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Describe your tattoo idea'})
    )

    class Meta:
        model = Booking
        fields = ['name', 'email', 'phone', 'artist', 'placement', 'description', 'reference', 'date']


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
