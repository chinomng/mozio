from django.contrib.gis import admin
from geoapi.models import Provider, Area

admin.site.register(Area, admin.GeoModelAdmin)
admin.site.register(Provider, admin.GeoModelAdmin)
