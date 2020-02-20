from django.urls import path

from city_list.views import CityListView

urlpatterns = [
    path('', CityListView.as_view(), name='city_list')
]
