from django import forms
from home.models import Location

CHOICES = ['Shelter', 'Zone', 'Transport', 'Supplies']


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ('address', 'addresstype', 'city', 'state')

        # create a widegets dictionary
        widget = {
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
            'addresstype': forms.Form(forms.ChoiceField(choices=CHOICES)),
        }
