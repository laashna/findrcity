import re
from collections import defaultdict
import requests
from bs4 import BeautifulSoup


def get_population_data():
    # make the request
    page = requests.get('https://en.wikipedia.org/wiki/List_of_United_States_cities_by_population')

    # make the soup parsing object
    soup = BeautifulSoup(page.content, 'html.parser')

    # select with table with population data
    population_table = soup.select_one('#mw-content-text > div > table:nth-child(18) > tbody')

    data = defaultdict()

    for row in population_table.select('tr'):
        # skip heading
        if row.th:
            continue

        # put all the cells in a list
        row_cells = [cell for cell in row.select('td')]

        # replace '[<ANY LETTER>]' followed by '\n' (literal) or '\n' (literal)
        city = re.sub('(\[\w\]\\n)|\\n', '', row_cells[1].text)

        # replace any , or whitespace. with global and multiline flag
        census_2010_population = int(re.sub(',|\s', '', row_cells[4].text, flags=re.MULTILINE | re.DOTALL))

        data[city] = census_2010_population

    return data
