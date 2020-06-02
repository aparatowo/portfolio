# Rafał Nitychoruk
from pprint import pprint
from datetime import datetime

data = [{'name': 'Wanda Czarnecka', 'join_date': '21-03-2010'}, {'name': 'Aneta Jakubowska', 'join_date': '12-02-2018'},
        {'name': 'Sylwia Kaźmierczak', 'join_date': '26-05-2011'}, {'name': 'Genowefa Lis', 'join_date': '08-08-2011'},
        {'name': 'Zofia Bąk', 'join_date': '17-05-2020'}, {'name': 'Agata Gajewska', 'join_date': '13-01-2016'},
        {'name': 'Mieczysław Adamczyk', 'join_date': '07-03-2018'},
        {'name': 'Robert Włodarczyk,', 'join_date': '07-12-2012'}, {'name': 'Agata Pawlak', 'join_date': '21-07-2016'},
        {'name': 'Michał Sobczak', 'join_date': '05-04-2015'}]


def sort_key(item):
    str_date = item['join_date']
    date = datetime.strptime(str_date, "%d-%m-%Y")
    return date


if __name__ == '__main__':
    sorted_by_date = sorted(data, key=sort_key)

    pprint(sorted_by_date)



    sorted_by_date_with_lambda = sorted(data, key=lambda s: datetime.strptime(s['join_date'], "%d-%m-%Y"))  # ustaw parametr `key` na lambdę, która robi to samo co `sort_key()`

    pprint(sorted_by_date_with_lambda)

    assert sorted_by_date == sorted_by_date_with_lambda
