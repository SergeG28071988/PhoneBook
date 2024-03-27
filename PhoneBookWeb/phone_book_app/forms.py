from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['last_name', 'first_name', 'date_of_birth', 'address', 'email', 'phone_number', 'category']
