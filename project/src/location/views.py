from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import City, Country, Address, Province
from .forms import CityForm, CountryForm, AddressForm, ProvinceForm


class CityListView(ListView):
    model = City


class CityCreateView(CreateView):
    model = City
    form_class = CityForm


class CityDetailView(DetailView):
    model = City


class CityUpdateView(UpdateView):
    model = City
    form_class = CityForm


class CountryListView(ListView):
    model = Country


class CountryCreateView(CreateView):
    model = Country
    form_class = CountryForm


class CountryDetailView(DetailView):
    model = Country


class CountryUpdateView(UpdateView):
    model = Country
    form_class = CountryForm


class AddressListView(ListView):
    model = Address


class AddressCreateView(CreateView):
    model = Address
    form_class = AddressForm


class AddressDetailView(DetailView):
    model = Address


class AddressUpdateView(UpdateView):
    model = Address
    form_class = AddressForm


class ProvinceListView(ListView):
    model = Province


class ProvinceCreateView(CreateView):
    model = Province
    form_class = ProvinceForm


class ProvinceDetailView(DetailView):
    model = Province


class ProvinceUpdateView(UpdateView):
    model = Province
    form_class = ProvinceForm

