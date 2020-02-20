from django.views.generic import TemplateView


class CityDetailView(TemplateView):
    template_name = 'city_detail/city_detail.html'
