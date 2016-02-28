from django.contrib.gis.db import models


class Area(models.Model):
    name = models.CharField(max_length=80)
    area = models.PolygonField()
    price = models.DecimalField(max_digits=8, decimal_places=3)
    provider = models.ForeignKey('Provider')

    def __str__(self):
        return self.name

class Provider(models.Model):
    name = models.CharField(max_length=80)
    lang = models.CharField(max_length=10)
    email_address = models.EmailField()
    phone_number = models.CharField(max_length=10)
    currency = models.CharField(max_length=3)

    def __str__(self):
        return self.name