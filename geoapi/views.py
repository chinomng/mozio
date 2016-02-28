from geoapi.serializers import NewAreaSerializer, AreaSerializer, ProviderSerializer
from geoapi.models import Area, Provider

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from django.contrib.gis.geos import Point


class AreaModelViewSet(viewsets.ModelViewSet):
    """
    Areas API. Create, delete, update, list and get an area
    """

    serializer_class = NewAreaSerializer
    queryset = Area.objects.all().order_by('name')
    partial = True
    http_method_names = ['post', 'get', 'update', 'delete']


class SearchAreas(APIView):
    """
    Retrieve areas that contain a certain point
    """

    def get(self, request, lat, long):
        areas = Area.objects.filter(area__contains=Point(float(long), float(lat)))
        serializer = AreaSerializer(areas, many=True)
        return Response(serializer.data)


class ProviderModelViewSet(viewsets.ModelViewSet):
    """
    Providers API. Create, delete, update, list and get operations for a provider
    """

    serializer_class = ProviderSerializer
    queryset = Provider.objects.all().order_by('name')
    http_method_names = ['post', 'get', 'update', 'delete']
