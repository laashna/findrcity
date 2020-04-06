from collections import defaultdict
import pytest
from data_collection.crime_scraper import get_crime_data
from data_collection.economy_scraper.economy_scraper import get_economy_data
from data_collection.population_scraper import get_population_data
from data_collection.walkscore_scraper.walkscore_scraper import get_walkscore_data
from data_collection.weather_scraper import get_weather_data, meta_data


@pytest.fixture(scope="module")
def weather_data():
    return get_weather_data()


@pytest.fixture(scope="module")
def weather_data_keys():
    keys_to_test = []
    for elem in meta_data:
        for field in elem['fields']:
            keys_to_test.append(field)

    keys_to_test.append('state')
    return keys_to_test


@pytest.fixture(scope="module")
def crime_data():
    return get_crime_data()


@pytest.fixture(scope="module")
def walkscore_data():
    return get_walkscore_data()


@pytest.fixture(scope="module")
def economy_data():
    return get_economy_data()


@pytest.fixture(scope="module")
def population_data():
    return get_population_data()


class TestWalkScoreScraper:
    # we want to test that the return type is always a defaultdict, since our model's
    # loaddata function is built around this data type
    def test_return_type_defaultdict(self, walkscore_data):
        assert type(walkscore_data) == defaultdict

    @pytest.mark.parametrize(
        "test_input,expected",
        [
            (['walkscore', 'transit_score', 'bike_score'], True),
            (['walkkscoore', 'transitscore', 'bikescore'], False),
            (['walk_score'], False),
            ([''], False),

        ],
    )
    def test_correct_keys_in_return(self, walkscore_data, test_input, expected):
        for city in walkscore_data:
            for key in walkscore_data[city]:
                assert (key in test_input) == expected

    def test_all_cities_have_walkscore(self, walkscore_data):
        for city in walkscore_data:
            walkscore = walkscore_data[city]['walkscore']
            assert (walkscore is not None and walkscore > 0) == True

    def test_all_cities_have_bike_score(self, walkscore_data):
        for city in walkscore_data:
            bike_score = walkscore_data[city]['bike_score']
            assert (bike_score is not None and bike_score > 0) == True


class TestWeatherScraper:
    # we want to test that the return type is always a defaultdict, since our model's
    # loaddata function is built around this data type
    def test_return_type_defaultdict(self, weather_data):
        assert type(weather_data) == defaultdict

    def test_correct_keys_in_return(self, weather_data, weather_data_keys):
        for city in weather_data:
            for key in weather_data[city]:
                assert (key in weather_data_keys) == True


class TestPopulationScraper:
    # we want to test that the return type is always a defaultdict, since our model's
    # loaddata function is built around this data type
    def test_return_type_defaultdict(self, population_data):
        assert type(population_data) == defaultdict

    def test_all_cities_have_not_none_value(self, population_data):
        for city in population_data:
            assert (population_data[city] is not None) == True


class TestCrimeScrapper:
    # we want to test that the return type is always a defaultdict, since our model's
    # loaddata function is built around this data type
    def test_return_type_defaultdict(self, crime_data):
        assert type(crime_data) == defaultdict

    @pytest.mark.parametrize(
        "test_input,expected",
        [
            (['total_violent_crimes',
              'murder',
              'rape',
              'robbery',
              'assault',
              'total_property_crimes',
              'burglary',
              'larceny_theft',
              'motor_vehicle_theft',
              'arson'], True),
            (['totalviolentcrime', 'burglarry', 'arrson'], False),
            (['murderr', 'robbie'], False),
            ([''], False),

        ],
    )
    def test_correct_keys_in_return(self, crime_data, test_input, expected):
        for city in crime_data:
            for key in crime_data[city]:
                assert (key in test_input) == expected


class TestEconomyScraper:
    # we want to test that the return type is always a defaultdict, since our model's
    # loaddata function is built around this data type
    def test_return_type_defaultdict(self, economy_data):
        assert type(economy_data) == defaultdict

    def test_all_cities_have_unemployment(self, economy_data):
        for city in economy_data:
            unemployment_rate = economy_data[city]
            assert (unemployment_rate is not None and unemployment_rate > 0) == True
