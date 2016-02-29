from geoapi import factories
from geoapi.factories import ProviderFactory, CaliforniaAreaFactory, UserFactory
from models import Provider, Area

from rest_framework import test
from rest_framework import status

from django.core.urlresolvers import reverse


class AreaTests(test.APITestCase):

    def setUp(self):
        self.client.force_authenticate(UserFactory.create())

    def test_search_areas(self):
        provider = ProviderFactory.create()
        california_area = CaliforniaAreaFactory.create(provider=provider)

        response = self.client.get(reverse('search_areas', kwargs={'long': '-120.65', 'lat': '37.5'}))
        self.assertEqual(california_area.name, response.data[0]['name'])

        response = self.client.get(reverse('search_areas', kwargs={'long': '-123.28', 'lat': '41.33'}))
        self.assertEqual(california_area.name, response.data[0]['name'])

        response = self.client.get(reverse('search_areas', kwargs={'long': '-117.04', 'lat': '33.94'}))
        self.assertEqual(california_area.name, response.data[0]['name'])

    def test_search_areas_fail(self):
        CaliforniaAreaFactory.create(provider=ProviderFactory.create())

        response = self.client.get(reverse('search_areas', kwargs={'long': '-110', 'lat': '40'}))
        self.assertEqual(0, len(response.data))

        response = self.client.get(reverse('search_areas', kwargs={'long': '-157', 'lat': '38'}))
        self.assertEqual(0, len(response.data))

        response = self.client.get(reverse('search_areas', kwargs={'long': '0.5', 'lat': '40'}))
        self.assertEqual(0, len(response.data))

    def test_area_post(self):
        california_dict = factories.get_california_area_dict(ProviderFactory.create())
        url = reverse('area-list')
        response = self.client.post(url, california_dict, format='json')

        area = Area.objects.get(pk=response.data.get("id"))
        self.assertEqual(area.name, california_dict["name"])
        self.assertEqual(area.provider.id, california_dict["provider"])
        self.assertEqual(area.price, california_dict["price"])


class ProviderTests(test.APITestCase):

    def setUp(self):
        self.client.force_authenticate(UserFactory.create())

    def test_provider_detail(self):
        prov = ProviderFactory.create()
        response = self.client.get(reverse('provider-detail', args=[prov.id]))
        self.assertTrue(status.is_success(response.status_code))
        self.assertEqual(prov.name, response.data["name"])

    def test_provider_delete(self):
        prov = ProviderFactory.create()
        self.assertEqual(1, Provider.objects.count())
        self.client.delete(reverse('provider-detail', args=[prov.id]))
        self.assertEqual(0, Provider.objects.count())

    def test_provider_post(self):
        prov = ProviderFactory.build()
        prov_dic = {
                "name": prov.name,
                "email_address": prov.email_address,
                "phone_number": prov.phone_number,
                "lang": prov.lang,
                "currency": prov.currency,
        }
        response = self.client.post(reverse('provider-list'), prov_dic)
        provider = Provider.objects.get(pk=response.data.get("id"))
        self.assertEqual(provider.name, prov_dic["name"])
        self.assertEqual(provider.email_address, prov_dic["email_address"])
        self.assertEqual(provider.phone_number, prov_dic["phone_number"])
        self.assertEqual(provider.lang, prov_dic["lang"])
        self.assertEqual(provider.currency, prov_dic["currency"])

    def test_provider_list(self):
        for i in range(50):
            ProviderFactory.create()
        url = reverse('provider-list')
        response = self.client.get(url)
        self.assertEquals(len(response.data), 50)
