from django.views.generic import TemplateView
from contexts.city_list_contexts import FILTER_CATEGORIES_CONTEXT, CITY_LIST_HEADERS_CONTEXT
from django.views.generic import ListView

from city_list.models import City


class CityListView(ListView):
    template_name = 'city_list/city_list.html'
    model = City
    context_object_name = 'cities'

    def get_context_data(self, **kwargs):
        context = super(CityListView, self).get_context_data(**kwargs)
        context['category'] = FILTER_CATEGORIES_CONTEXT
        context['city_list_headers'] = CITY_LIST_HEADERS_CONTEXT
        return context
