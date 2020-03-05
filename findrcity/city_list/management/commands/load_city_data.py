from django.core.management import BaseCommand

from city_list.data_loaders.load_crime_data import load_crime_data
from city_list.data_loaders.load_population_data import load_population_data
from city_list.data_loaders.load_walkscore_data import load_walkscore_data
from city_list.data_loaders.load_weather_data import load_weather_data


class Command(BaseCommand):
    help = 'Sync FindrCity Cities'

    def handle(self, *args, **options):
        self.load_city_data()

    @staticmethod
    def load_city_data():
        load_weather_data()
        load_population_data()
        load_walkscore_data()
        load_crime_data()

