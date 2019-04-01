from . import models
from . import serializers
from rest_framework import viewsets, permissions


class CityViewSet(viewsets.ModelViewSet):
    """ViewSet for the City class"""

    queryset = models.City.objects.all()
    serializer_class = serializers.CitySerializer
    permission_classes = [permissions.IsAuthenticated]


class CountryViewSet(viewsets.ModelViewSet):
    """ViewSet for the Country class"""

    queryset = models.Country.objects.all()
    serializer_class = serializers.CountrySerializer
    permission_classes = [permissions.IsAuthenticated]


class AddressViewSet(viewsets.ModelViewSet):
    """ViewSet for the Address class"""

    queryset = models.Address.objects.all()
    serializer_class = serializers.AddressSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProvinceViewSet(viewsets.ModelViewSet):
    """ViewSet for the Province class"""

    queryset = models.Province.objects.all()
    serializer_class = serializers.ProvinceSerializer
    permission_classes = [permissions.IsAuthenticated]


