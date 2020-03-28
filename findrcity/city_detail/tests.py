from django.test import TestCase
from django.urls import reverse


class TestCityDetail(TestCase):
    def test_call_city_detail(self):
        response = self.client.get(reverse('city_detail'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'city_detail/city_detail.html')