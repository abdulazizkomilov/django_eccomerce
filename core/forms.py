from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget

PAYMENT_CHOICES = (
    ('S', 'Stripe'),
    ('P', 'PayPal'),
)

CHOICE_LIST = [
    ('', 'Choose...'),
    (1, 'Tashkent'),
    (2, 'Samarkand'),
    (3, 'Navoiy'),
]


class CheckoutForm(forms.Form):
    street_address = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': '...'
    }))
    apartment_adddress = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'placeholder': '...'
    }))
    country = CountryField(blank_label='(select country)').formfield(
        widget=CountrySelectWidget(attrs={
        'class':'custom-select d-block w-100',
    }))
    region = forms.ChoiceField(choices=CHOICE_LIST, required=False)
    zip = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))
    # same_billing_address = forms.BooleanField(required=False)
    # save_info = forms.BooleanField(required=False)
    payment_option = forms.ChoiceField(
        widget=forms.RadioSelect, choices=PAYMENT_CHOICES)
