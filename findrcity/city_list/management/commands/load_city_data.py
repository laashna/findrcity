from django.core.management import BaseCommand

from city_list.data_loaders.load_weather_data import load_weather_data


class Command(BaseCommand):
    help = 'Sync FindrCity Cities'

    def handle(self, *args, **options):
        self.load_city_data()

    @staticmethod
    def load_city_data():
        load_weather_data()

