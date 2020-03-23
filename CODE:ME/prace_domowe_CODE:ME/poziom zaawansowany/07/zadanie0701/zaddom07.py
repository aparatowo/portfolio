# Rafał Nitychoruk
from flask import Flask, render_template
import json

app = Flask(__name__)


def pobierz_dane():
    with open('ludzie.json') as f:
        return json.load(f)


@app.route('/')
def index():
    lista_osob = pobierz_dane()

    return render_template('lista.html', lista_osob=lista_osob)


@app.route('/osoba/<int:indeks>')
def osoba(indeks):
    users = pobierz_dane()
    try:
        user = [user for user in users if user['id'] == int(indeks)]
        context = user[0]
    except IndexError:
        context = {'error': f'Brak osoby o ID:{indeks}.'}

    return render_template('osoba.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
