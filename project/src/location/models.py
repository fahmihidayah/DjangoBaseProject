from django.urls import reverse
from django_extensions.db.fields import AutoSlugField
from django.db.models import CharField
from django.db.models import DateTimeField
from django.db.models import FloatField
from django_extensions.db.fields import AutoSlugField
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_models
from django.db import models as models
from django_extensions.db import fields as extension_fields


class City(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    # Relationship Fields
    country = models.ForeignKey(
        'location.Country',
        on_delete=models.CASCADE, related_name="citys", 
    )

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('location_city_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('location_city_update', args=(self.slug,))


class Country(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)


    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('location_country_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('location_country_update', args=(self.slug,))


class Address(models.Model):

    # Fields
    street_name = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='street_name', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    rt = models.CharField(max_length=30)
    rw = models.CharField(max_length=30)
    longitude = models.FloatField()
    latitude = models.FloatField()
    postal_code = models.CharField(max_length=30)
    building_number = models.CharField(max_length=100)

    # Relationship Fields
    city = models.ForeignKey(
        'location.City',
        on_delete=models.CASCADE, related_name="addresss", 
    )
    country = models.ForeignKey(
        'location.Country',
        on_delete=models.CASCADE, related_name="addresss", 
    )
    province = models.ForeignKey(
        'location.Province',
        on_delete=models.CASCADE, related_name="addresss", 
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, related_name="addresss", 
    )

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('location_address_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('location_address_update', args=(self.slug,))


class Province(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)


    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('location_province_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('location_province_update', args=(self.slug,))


