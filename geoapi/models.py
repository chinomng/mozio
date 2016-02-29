from django.contrib.gis.db import models
from django.core.validators import RegexValidator


class Area(models.Model):
    name = models.CharField(max_length=80)
    provider = models.ForeignKey('Provider')
    area = models.PolygonField()
    price = models.DecimalField(max_digits=8, decimal_places=3)

    def __str__(self):
        return self.name


class Provider(models.Model):
    name = models.CharField(max_length=80)
    lang = models.CharField(max_length=10)
    email_address = models.EmailField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(max_length=15, validators=[phone_regex])
    currency = models.CharField(max_length=3)

    def __str__(self):
        return self.name
