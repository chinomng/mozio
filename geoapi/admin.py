from django.contrib.gis import admin
from .models import Provider, Area

admin.site.register(Provider, admin.GeoModelAdmin)
admin.site.register(Area, admin.GeoModelAdmin)