from django import forms
from .models import City, Country, Address, Province


class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ['name', 'country']


class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = ['name']


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['street_name', 'rt', 'rw', 'longitude', 'latitude', 'postal_code', 'building_number', 'city', 'country', 'province', 'user']


class ProvinceForm(forms.ModelForm):
    class Meta:
        model = Province
        fields = ['name']


