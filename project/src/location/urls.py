from django.urls import path, include
from rest_framework import routers

from . import api
from . import views

router = routers.DefaultRouter()
router.register(r'city', api.CityViewSet)
router.register(r'country', api.CountryViewSet)
router.register(r'address', api.AddressViewSet)
router.register(r'province', api.ProvinceViewSet)


urlpatterns = (
    # urls for Django Rest Framework API
    path('api/v1/', include(router.urls)),
)

urlpatterns += (
    # urls for City
    path('location/city/', views.CityListView.as_view(), name='location_city_list'),
    path('location/city/create/', views.CityCreateView.as_view(), name='location_city_create'),
    path('location/city/detail/<slug:slug>/', views.CityDetailView.as_view(), name='location_city_detail'),
    path('location/city/update/<slug:slug>/', views.CityUpdateView.as_view(), name='location_city_update'),
)

urlpatterns += (
    # urls for Country
    path('location/country/', views.CountryListView.as_view(), name='location_country_list'),
    path('location/country/create/', views.CountryCreateView.as_view(), name='location_country_create'),
    path('location/country/detail/<slug:slug>/', views.CountryDetailView.as_view(), name='location_country_detail'),
    path('location/country/update/<slug:slug>/', views.CountryUpdateView.as_view(), name='location_country_update'),
)

urlpatterns += (
    # urls for Address
    path('location/address/', views.AddressListView.as_view(), name='location_address_list'),
    path('location/address/create/', views.AddressCreateView.as_view(), name='location_address_create'),
    path('location/address/detail/<slug:slug>/', views.AddressDetailView.as_view(), name='location_address_detail'),
    path('location/address/update/<slug:slug>/', views.AddressUpdateView.as_view(), name='location_address_update'),
)

urlpatterns += (
    # urls for Province
    path('location/province/', views.ProvinceListView.as_view(), name='location_province_list'),
    path('location/province/create/', views.ProvinceCreateView.as_view(), name='location_province_create'),
    path('location/province/detail/<slug:slug>/', views.ProvinceDetailView.as_view(), name='location_province_detail'),
    path('location/province/update/<slug:slug>/', views.ProvinceUpdateView.as_view(), name='location_province_update'),
)

