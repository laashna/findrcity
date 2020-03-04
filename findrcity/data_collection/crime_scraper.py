import re
from collections import defaultdict
import requests
from bs4 import BeautifulSoup


def clean_data(data):
    if data == '':
        return data
    else:
        return float(data)


def get_crime_data():
    page = requests.get('https://en.wikipedia.org/wiki/List_of_United_States_cities_by_crime_rate')

    soup = BeautifulSoup(page.content, 'html.parser')

    crime_table = soup.select_one('#mw-content-text > div > table > tbody')

    nested_data = lambda: defaultdict(nested_data)
    data = nested_data()
    # data = defaultdict()

    for row in crime_table.select('tr'):

        if row.th:
            continue

        row_cells = [cell for cell in row.select('td')]

        city_original = row_cells[1].text
        # Remove superscripts from city name
        city = ''.join([i for i in city_original if not i.isdigit() and i != ','])

        data[city]['total_violent_crimes'] = clean_data(row_cells[3].text)
        data[city]['murder'] = clean_data(row_cells[4].text)
        data[city]['rape'] = clean_data(row_cells[5].text)
        data[city]['robbery'] = clean_data(row_cells[6].text)
        data[city]['assault'] = clean_data(row_cells[7].text)
        data[city]['total_property_crimes'] = clean_data(row_cells[8].text)
        data[city]['burglary'] = clean_data(row_cells[9].text)
        data[city]['larceny_theft'] = clean_data(row_cells[10].text)
        data[city]['motor_vehicle_theft'] = clean_data(row_cells[11].text)
        # Remove newline character on the end of line cell
        data[city]['arson'] = clean_data(re.sub('\\n', '', row_cells[12].text))

    return data


get_crime_data()
