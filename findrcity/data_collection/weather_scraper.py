import requests
from bs4 import BeautifulSoup
from collections import defaultdict

"""
meta data for scraping weather data with a single function
type: list of dictionaries

{
    'url' - the url of the page to scrape
}
"""
meta_data = [
    # temperature
    {
        'url': 'https://www.currentresults.com/Weather/US/average-annual-temperatures-large-cities.php',
        'city_pos': 2,
        'fields': {'temperature_high': 0, 'temperature_low': 1}
    },

    # precipitation
    {
        'url': 'https://www.currentresults.com/Weather/US/average-annual-precipitation-by-city.php',
        'city_pos': 1,
        'fields': {'precipitation_days': 0, 'precipitation_inches': 2}
    },

    # snowfall
    {
        'url': 'https://www.currentresults.com/Weather/US/annual-snowfall-by-city.php',
        'city_pos': 1,
        'fields': {'snowfall_days': 0, 'snowfall_inches': 2}

    },

    # sunshine
    {
        'url': 'https://www.currentresults.com/Weather/US/average-annual-sunshine-by-city.php',
        'city_pos': 1,
        'fields': {'sunshine_percent': 0, 'sunshine_hours': 2, 'sunshine_clear_days': 3}
    },

    # cloud & fog
    {
        'url': 'https://www.currentresults.com/Weather/US/cloud-fog-city-annual.php',
        'city_pos': 0,
        'fields': {'cloud_days': 1, 'fog_days': 2}
    },

    # wind
    {
        'url': 'https://www.currentresults.com/Weather/US/wind-speed-city-annual.php',
        'city_pos': 0,
        'fields': {'wind_mph': 1}
    }

]

# using nested dict to prevent key errors
nested_data = lambda: defaultdict(nested_data)
data = nested_data()

for page_to_scrape in meta_data:

    # make the request
    page = requests.get(page_to_scrape['url'])

    # make the soup object
    soup = BeautifulSoup(page.content, 'html.parser')

    # find all tables in the page with weather info in them
    weather_tables = soup.find_all('table', class_='articletable')

    # for each table that has weather data (there are usually 3 on the site)
    for table in weather_tables:
        # for each row in that table
        for row in table.select('tr'):
            # skip table headings
            if row.th:
                continue

            row_contents = [item for item in row.stripped_strings]

            for field in page_to_scrape['fields']:
                city_state = row_contents[page_to_scrape['city_pos']]

                city = city_state[:city_state.find(',')]
                state = city_state[city_state.find(','):].strip(', ')

                data[city][field] = row_contents[page_to_scrape['fields'][field]]
                data[city]['state'] = state

