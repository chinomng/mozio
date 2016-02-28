from geoapi.models import Area, Provider

from rest_framework_gis.serializers import GeoFeatureModelSerializer
from rest_framework import serializers

class AreaSerializer(serializers.HyperlinkedModelSerializer):
    provider = serializers.StringRelatedField()

    class Meta:
        model = Area
        fields = ('name', 'provider', 'price')


class NewAreaSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Area
        fields = ('id', 'name', 'provider', 'area', 'price')
        geo_field = 'area'


class ProviderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Provider
        fields = ('id', 'name', 'lang', 'email_address', 'phone_number', 'currency')
