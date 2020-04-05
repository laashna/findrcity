from django.urls import path
from city_detail.views import Info

urlpatterns = [
    path('<int:pk>', Info.as_view(), name="info")  # int:pk is showing the primary key for the specific database object
]
