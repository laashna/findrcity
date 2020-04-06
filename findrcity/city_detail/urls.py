from django.urls import path
from city_detail.views import CityDetailView

urlpatterns = [
    path('<str:name>', CityDetailView.as_view(), name="city")
]
