from geoapi import views

from rest_framework import routers

from django.conf.urls import url, include


router = routers.DefaultRouter()
router.register(r'area', views.AreaModelViewSet, 'area')
router.register(r'provider', views.ProviderModelViewSet, 'provider')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^search_areas/(?P<lat>(\-?\d+(\.\d+)?))/(?P<long>(\-?\d+(\.\d+)?))/$',
        views.SearchAreas.as_view(), name='search_areas'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
