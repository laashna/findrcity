from django.template.defaultfilters import slugify
from django.views.generic import DetailView
from city_list.models import City, State


class CityDetailView(DetailView):
    template_name = 'city_detail/city_detail.html'
    model = City
    context_object_name = "city"  # name of the object of the html
    slug_field = "name"
    slug_url_kwarg = "name"

