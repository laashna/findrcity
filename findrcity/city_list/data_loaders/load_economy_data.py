from city_list.models import City
from data_collection.economy_scraper.economy_scraper import get_economy_data

def load_economy_data():
    economy_data = get_economy_data()

    for record in economy_data:
        if City.objects.filter(name=record).exists():
            city_instance = City.objects.get(name=record)
        else:
            continue

        for data in economy_data[record]:
            try:
                city_instance.__dict__[data] = economy_data[record][data]
            except ValueError:
                continue
            city_instance.save()
