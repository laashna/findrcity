from django.test import TestCase
from django.urls import reverse


class TestCityList(TestCase):
    def test_call_city_list(self):
        response = self.client.get(reverse('city_list'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'city_list/city_list.html')
