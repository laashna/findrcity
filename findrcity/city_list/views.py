from django.views.generic import TemplateView


class CityListView(TemplateView):
    template_name = 'city_list/city_list.html'
