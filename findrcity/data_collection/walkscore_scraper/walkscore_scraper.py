import re
from collections import defaultdict
from bs4 import BeautifulSoup


def clean_score(score):
    try:
        cleaned_score = float(score.string.strip())
    except ValueError:
        cleaned_score = None

    return cleaned_score


def get_walkscore_data():
    soup = BeautifulSoup(open('walkscore_table.html'), 'html.parser')

    table = soup.find('tbody')

    # nested default dict
    nested_data = lambda: defaultdict(nested_data)
    data = nested_data()

    # for each row in the table
    for row in table.select('tr'):
        city = row.select_one('td.city').string.strip()
        data[city]['state'] = row.select_one('td.state').string.strip()

        data[city]['walkscore'] = clean_score(score=row.select_one('td.score'))
        data[city]['transit_score'] = clean_score(score=row.select_one('td.tsc'))
        data[city]['bike_score'] = clean_score(score=row.select_one('td.bsc'))

    return data

