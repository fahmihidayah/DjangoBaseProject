from django.contrib import admin
from django import forms
from .models import City, Country, Address, Province

class CityAdminForm(forms.ModelForm):

    class Meta:
        model = City
        fields = '__all__'


class CityAdmin(admin.ModelAdmin):
    form = CityAdminForm
    list_display = ['name', 'slug', 'created', 'last_updated']
    readonly_fields = ['name', 'slug', 'created', 'last_updated']

admin.site.register(City, CityAdmin)


class CountryAdminForm(forms.ModelForm):

    class Meta:
        model = Country
        fields = '__all__'


class CountryAdmin(admin.ModelAdmin):
    form = CountryAdminForm
    list_display = ['name', 'slug', 'created', 'last_updated']
    readonly_fields = ['name', 'slug', 'created', 'last_updated']

admin.site.register(Country, CountryAdmin)


class AddressAdminForm(forms.ModelForm):

    class Meta:
        model = Address
        fields = '__all__'


class AddressAdmin(admin.ModelAdmin):
    form = AddressAdminForm
    list_display = ['street_name', 'slug', 'created', 'last_updated', 'rt', 'rw', 'longitude', 'latitude', 'postal_code', 'building_number']
    readonly_fields = ['street_name', 'slug', 'created', 'last_updated', 'rt', 'rw', 'longitude', 'latitude', 'postal_code', 'building_number']

admin.site.register(Address, AddressAdmin)


class ProvinceAdminForm(forms.ModelForm):

    class Meta:
        model = Province
        fields = '__all__'


class ProvinceAdmin(admin.ModelAdmin):
    form = ProvinceAdminForm
    list_display = ['name', 'slug', 'created', 'last_updated']
    readonly_fields = ['name', 'slug', 'created', 'last_updated']

admin.site.register(Province, ProvinceAdmin)


