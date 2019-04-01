import unittest
from django.urls import reverse
from django.test import Client
from .models import City, Country, Address, Province
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType


def create_django_contrib_auth_models_user(**kwargs):
    defaults = {}
    defaults["username"] = "username"
    defaults["email"] = "username@tempurl.com"
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_django_contrib_auth_models_group(**kwargs):
    defaults = {}
    defaults["name"] = "group"
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_django_contrib_contenttypes_models_contenttype(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_city(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults.update(**kwargs)
    if "country" not in defaults:
        defaults["country"] = create_country()
    return City.objects.create(**defaults)


def create_country(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults.update(**kwargs)
    return Country.objects.create(**defaults)


def create_address(**kwargs):
    defaults = {}
    defaults["street_name"] = "street_name"
    defaults["rt"] = "rt"
    defaults["rw"] = "rw"
    defaults["longitude"] = "longitude"
    defaults["latitude"] = "latitude"
    defaults["postal_code"] = "postal_code"
    defaults["building_number"] = "building_number"
    defaults.update(**kwargs)
    if "city" not in defaults:
        defaults["city"] = create_city()
    if "country" not in defaults:
        defaults["country"] = create_country()
    if "province" not in defaults:
        defaults["province"] = create_province()
    if "user" not in defaults:
        defaults["user"] = create_django_contrib_auth_models_user()
    return Address.objects.create(**defaults)


def create_province(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults.update(**kwargs)
    return Province.objects.create(**defaults)


class CityViewTest(unittest.TestCase):
    '''
    Tests for City
    '''
    def setUp(self):
        self.client = Client()

    def test_list_city(self):
        url = reverse('location_city_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_city(self):
        url = reverse('location_city_create')
        data = {
            "name": "name",
            "country": create_country().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_city(self):
        city = create_city()
        url = reverse('location_city_detail', args=[city.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_city(self):
        city = create_city()
        data = {
            "name": "name",
            "country": create_country().pk,
        }
        url = reverse('location_city_update', args=[city.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class CountryViewTest(unittest.TestCase):
    '''
    Tests for Country
    '''
    def setUp(self):
        self.client = Client()

    def test_list_country(self):
        url = reverse('location_country_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_country(self):
        url = reverse('location_country_create')
        data = {
            "name": "name",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_country(self):
        country = create_country()
        url = reverse('location_country_detail', args=[country.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_country(self):
        country = create_country()
        data = {
            "name": "name",
        }
        url = reverse('location_country_update', args=[country.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class AddressViewTest(unittest.TestCase):
    '''
    Tests for Address
    '''
    def setUp(self):
        self.client = Client()

    def test_list_address(self):
        url = reverse('location_address_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_address(self):
        url = reverse('location_address_create')
        data = {
            "street_name": "street_name",
            "rt": "rt",
            "rw": "rw",
            "longitude": "longitude",
            "latitude": "latitude",
            "postal_code": "postal_code",
            "building_number": "building_number",
            "city": create_city().pk,
            "country": create_country().pk,
            "province": create_province().pk,
            "user": create_django_contrib_auth_models_user().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_address(self):
        address = create_address()
        url = reverse('location_address_detail', args=[address.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_address(self):
        address = create_address()
        data = {
            "street_name": "street_name",
            "rt": "rt",
            "rw": "rw",
            "longitude": "longitude",
            "latitude": "latitude",
            "postal_code": "postal_code",
            "building_number": "building_number",
            "city": create_city().pk,
            "country": create_country().pk,
            "province": create_province().pk,
            "user": create_django_contrib_auth_models_user().pk,
        }
        url = reverse('location_address_update', args=[address.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class ProvinceViewTest(unittest.TestCase):
    '''
    Tests for Province
    '''
    def setUp(self):
        self.client = Client()

    def test_list_province(self):
        url = reverse('location_province_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_province(self):
        url = reverse('location_province_create')
        data = {
            "name": "name",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_province(self):
        province = create_province()
        url = reverse('location_province_detail', args=[province.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_province(self):
        province = create_province()
        data = {
            "name": "name",
        }
        url = reverse('location_province_update', args=[province.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


