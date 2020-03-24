from city_list.models import City
from data_collection.population_scraper import get_population_data


def load_population_data():
    population_data = get_population_data()

    for record in population_data:
        if City.objects.filter(name=record).exists():
            city_instance = City.objects.get(name=record)
            city_instance.population = population_data[record]
            city_instance.save()
        else:
            continue