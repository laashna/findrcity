# from city_list.models import City
from city_list.models import City, State
from data_collection.weather_scraper import get_weather_data
from data_collection.population_scraper import get_population_data

def load_weather_data():
    weather_data = get_weather_data()

    for record in weather_data:
        if City.objects.filter(name=record).exists():
            city_instance = City.objects.get(name=record)
        else:
            city_instance = City()
            city_instance.name = record

        if State.objects.filter(name=weather_data[record]['state']).exists():
            state_instance = State.objects.get(name=weather_data[record]['state'])
        else:
            state_instance = State()

        for data in weather_data[record]:
            if data != 'state':
                try:
                    city_instance.__dict__[data] = float(weather_data[record][data])
                except ValueError:
                    continue

            if data == 'state':
                if State.objects.filter(name=weather_data[record][data]).exists():
                    continue
                else:
                    state_instance.name = weather_data[record][data]

        state_instance.save()
        city_instance.state = state_instance
        city_instance.save()


load_weather_data()
