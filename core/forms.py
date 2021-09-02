from django import forms
from django_countries.fields import CountryField
from django.forms import ChoiceField

PAYMENT_CHOICES = (
    ('S', 'Stripe'),
    ('P', 'PayPal'),
)

CHOICE_LIST = [
    ('', 'Choose...'),
    (1, 'Tashkent'),
    (2, 'Samarkand'),
]


class CheckoutForm(forms.Form):
    street_address = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': '1234 Main St'
    }))
    apartment_adddress = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'placeholder': 'Apartment or suite'
    }))
    country = CountryField(blank_label='(select country)').formfield(attrs={
        'class': 'custom-select d-block w-100'
    })
    region = ChoiceField(choices=CHOICE_LIST, required=False)
    zip = forms.CharField()
    same_billing_address = forms.BooleanField(required=False)
    save_info = forms.BooleanField(required=False)
    payment_option = forms.ChoiceField(
        widget=forms.RadioSelect, choices=PAYMENT_CHOICES)
