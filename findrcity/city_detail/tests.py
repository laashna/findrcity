from django.test import TestCase
from django.urls import reverse

from city_list.models import State, City


class TestCityDetail(TestCase):
    @classmethod
    def setUpTestData(cls):
        State.objects.create(name='Louisiana')
        City.objects.create(name='Lafayette', temperature_high=100, state=State.objects.get(name='Louisiana'))

    def test_city_detail_url_config(self):
        response = self.client.get(reverse('city_detail', args=['Lafayette']), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'city_detail/city_detail.html')