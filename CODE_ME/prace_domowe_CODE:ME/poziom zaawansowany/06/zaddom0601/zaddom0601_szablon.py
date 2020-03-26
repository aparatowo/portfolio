# imię i nazwisko

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    # tu wpisz swój kod
    return render_template('index.html')


@app.route('/add')
def add_number():
    number = None  # zamień tę linijkę na swój kod
    return f'Liczba {number} dodana!'


@app.route('/numbers')
def print_numbers():
    # tu wpisz swój kod
    return ''


if __name__ == '__main__':
    app.run(debug=True)
