from django.views.generic import TemplateView
from django.views.generic import ListView

from city_list.models import City


class CityListView(ListView):
    template_name = 'city_list/city_list.html'
    model = City
    context_object_name = 'city'
