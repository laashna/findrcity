from city_list.models import City
from data_collection.crime_scraper import get_crime_data


def load_crime_data():
    crime_data = get_crime_data()

    for record in crime_data:
        if City.objects.filter(name=record).exists():
            city_instance = City.objects.get(name=record)

            for data in crime_data[record]:
                try:
                    city_instance.__dict__[data] = float(crime_data[record][data])
                except ValueError:
                    continue

            city_instance.save()
        else:
            continue