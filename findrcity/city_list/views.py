from django.views.generic import TemplateView
from contexts.city_list_contexts import FILTER_CATEGORIES_CONTEXT


class CityListView(TemplateView):
    template_name = 'city_list/city_list.html'

    def get_context_data(self, **kwargs):
        context = super(CityListView, self).get_context_data(**kwargs)
        context['category'] = FILTER_CATEGORIES_CONTEXT
        return context
