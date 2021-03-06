# Rafał Nitychoruk

from flask import Flask, render_template, request
import json

app = Flask(__name__)


@app.route('/', methods=['get'])
def index():
    all_numbers = []
    try:
        with open('database.json', mode='r') as numbers_database:
            all_numbers = json.load(numbers_database)
    except FileNotFoundError:
        with open('database.json', mode='w') as numbers_database:
            json.dump(all_numbers, numbers_database)
    num_list_len = len(all_numbers)

    return render_template('index.html', all_numbers=all_numbers, num_list_len=num_list_len)


@app.route('/add', methods=['post'])
def add_number():
    number = request.form.get('integer_from_form')
    with open('database.json', mode='r') as numbers_database:
        whole_data = json.load(numbers_database)
    whole_data.append(int(number))

    with open('database.json', mode='w') as numbers_database:
        json.dump(whole_data, numbers_database)
    return f'Liczba {number} dodana!'


@app.route('/numbers/', methods=['get'])
def print_numbers():
    data = request.args.get('data')

    with open('database.json', mode='r') as numbers_database:
        whole_data = json.load(numbers_database)

    if data == 'DSC':
        whole_data.sort(reverse=True)
    elif data == 'ASC':
        whole_data.sort(reverse=False)

    return f'{whole_data}'


if __name__ == '__main__':
    app.run(debug=True)
