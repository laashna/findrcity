from city_list.models import City
from data_collection.economy_scraper.economy_scraper import get_economy_data

def load_economy_data():
    economy_data = get_economy_data()

    for record in economy_data:
        if City.objects.filter(name=record).exists():
            city_instance = City.objects.get(name=record)
            city_instance.unemployment_rate = economy_data[record]
            city_instance.save()
        else:
            continue
