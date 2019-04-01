from . import models

from rest_framework import serializers


class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.City
        fields = (
            'slug', 
            'name', 
            'created', 
            'last_updated', 
        )


class CountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Country
        fields = (
            'slug', 
            'name', 
            'created', 
            'last_updated', 
        )


class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Address
        fields = (
            'slug', 
            'street_name', 
            'created', 
            'last_updated', 
            'rt', 
            'rw', 
            'longitude', 
            'latitude', 
            'postal_code', 
            'building_number', 
        )


class ProvinceSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Province
        fields = (
            'slug', 
            'name', 
            'created', 
            'last_updated', 
        )


