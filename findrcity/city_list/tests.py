from django.test import TestCase
from django.urls import reverse
from city_list.models import City, State


class TestCityList(TestCase):
    def test_call_city_list(self):
        response = self.client.get(reverse('city_list'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'city_list/city_list.html')


class TestCityModel(TestCase):
    @classmethod
    def setUpTestData(cls):
        State.objects.create(name='Louisiana')
        City.objects.create(name='Lafayette', temperature_high=100, state=State.objects.get(name='Louisiana'))

    def test_city_url(self):
        city = City.objects.get(id=1)
        self.assertEquals(city.get_absolute_url(), '/detail/Lafayette')

    def test_city_name_length(self):
        city = City.objects.get(id=1)
        max_length = city._meta.get_field('name').max_length
        self.assertEquals(max_length, 100)

    def test_city_state_relation(self):
        city = City.objects.get(id=1)
        self.assertEquals(city.get_state_name(), 'Louisiana')