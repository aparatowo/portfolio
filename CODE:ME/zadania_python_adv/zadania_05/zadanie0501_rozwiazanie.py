from flask import Flask

app = Flask(__name__)


@app.route('/odczyt')
def read_from_file():
    try:
        with open('database.txt') as f:
            data = f.read()
            return f'Dane w bazie to: "{data}"'
    except FileNotFoundError:
        return 'Najpierw zapisz coś do bazy!'


@app.route('/zapis/<data>')
def write_to_file(data):
    with open('database.txt', mode='w', encoding='utf8') as f:
        f.write(data)
        return f'Zapisano do bazy dane: "{data}"'


if __name__ == "__main__":
    app.run()
