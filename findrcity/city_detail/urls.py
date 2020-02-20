from django.urls import path
from city_detail.views import CityDetailView

urlpatterns = [
    path('', CityDetailView.as_view(), name='city_detail')
]
