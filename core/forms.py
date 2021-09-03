from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget

PAYMENT_CHOICES = (
    ('S', 'Stripe'),
    ('P', 'PayPal'),
)

CHOICE_LIST = [
    ('', 'Choose...'),
    (1, 'Andijan'),
    (2, 'Buxoro'),
    (3, 'Fargana'),
    (4, 'Jizzax'),
    (5, 'Namangan'),
    (6, 'Navoiy'),
    (7, 'Qashqadaryo'),
    (8, 'Qoraqalpagistan'),
    (9, 'Samarkand'),
    (10, 'Sirdaryo'),
    (11, 'Surxandaryo'),
    (12, 'Tashkent'),
]


class CheckoutForm(forms.Form):
    street_address = forms.CharField(required=False)
    apartment_adddress = forms.CharField(required=False)
    country = CountryField(blank_label='(select country)').formfield(
        widget=CountrySelectWidget(attrs={
        'class':'custom-select d-block w-100',
    }))
    region = forms.ChoiceField(choices=CHOICE_LIST, required=False)
    zip = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))
    same_shipping_address = forms.BooleanField(required=False)
    save_info = forms.BooleanField(required=False)
    payment_option = forms.ChoiceField(
        widget=forms.RadioSelect, choices=PAYMENT_CHOICES)
