from geoapi.models import Area, Provider

from django.contrib.gis.geos import GEOSGeometry
from django.contrib.auth.models import User

import random
import string
import factory
import json


def random_string(length=10):
    return u''.join(random.choice(string.ascii_letters) for x in range(length))

def get_california_area():
    return {
            "type": "Polygon",
            "coordinates": [
                    [
                        [
                            -124.28613334894,
                            42.152344286442
                        ],
                        [
                            -120.15527397394,
                            42.020508348942
                        ],
                        [
                            -119.93554741144,
                            38.988281786442
                        ],
                        [
                            -114.88183647394,
                            35.340820848942
                        ],
                        [
                            -114.31054741144,
                            34.110352098942
                        ],
                        [
                            -117.03515678644,
                            32.704102098942
                        ],
                        [
                            -122.13281303644,
                            36.395508348942
                        ],
                        [
                            -122.26464897394,
                            36.615234911442
                        ],
                        [
                            -124.28613334894,
                            42.152344286442
                        ]
                    ]
                ]
        }

def get_california_area_dict(provider):
        return {
            "name": "California",
            "area": get_california_area(),
            "price": 650.00,
            "provider": provider.id
        }


class UserFactory(factory.Factory):
    class Meta:
        model = User

    username = factory.LazyAttribute(lambda t: random_string(50))
    password = factory.LazyAttribute(lambda t: random_string(50))


class CaliforniaAreaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Area

    name = factory.LazyAttribute(lambda t: random_string(50))
    area = factory.LazyAttribute(lambda a: GEOSGeometry(json.dumps(get_california_area())))
    price = 80


class ProviderFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Provider

    name = factory.LazyAttribute(lambda t: random_string(50))
    lang = 'EN'
    email_address = factory.LazyAttribute(lambda a: '{0}@example.com'.format(a.name).lower())
    phone_number = factory.Sequence(lambda n: '12355577%04d' % n)
    currency = 'USD'
