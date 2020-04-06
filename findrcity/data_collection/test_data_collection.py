from collections import defaultdict
import pytest

from data_collection.walkscore_scraper.walkscore_scraper import get_walkscore_data


@pytest.fixture(scope="module")
def walkscore_data():
    return get_walkscore_data()


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
