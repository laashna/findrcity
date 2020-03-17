from collections import defaultdict
from bs4 import BeautifulSoup


# Remove city names after comma, dash, or slash
def get_city(data):
    data = data.split("-")[0]
    data = data.split(",")[0]
    data = data.split("/")[0]
    return data


def get_economy_data():
    soup = BeautifulSoup(open("data_collection/economy_scraper/unemployment_table.html"), "html.parser")
    data = defaultdict()

    for row in soup.select('tr'):
        city = get_city(row.p.text)
        row_cells = [cell for cell in row.select('td')]
        data[city] = float(row_cells[0].text)

    return data
