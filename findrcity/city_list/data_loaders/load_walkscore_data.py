from city_list.models import City
from data_collection.walkscore_scraper.walkscore_scraper import get_walkscore_data


def load_walkscore_data():
    walkscore_data = get_walkscore_data()

    for record in walkscore_data:
        if City.objects.filter(name=record).exists():
            city_instance = City.objects.get(name=record)
        else:
            continue

        for data in walkscore_data[record]:
            try:
                city_instance.__dict__[data] = walkscore_data[record][data]
            except ValueError:
                continue
        city_instance.save()