from django.views.generic import DetailView
from city_list.models import City, State


class Info(DetailView):
    template_name = 'city_detail/city_detail.html'
    model = City
    context_object_name = "info"  # name of the object of the html
