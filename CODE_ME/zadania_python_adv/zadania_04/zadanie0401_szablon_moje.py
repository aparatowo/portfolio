import json

class JSONData:
    def __enter__(self):
        self.data = read_json()
        return self.data

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

def read_json():
    try:
        file = open('data.json', mode='r')
        data = json.load(file)
        file.close()
        return data
    except FileNotFoundError:
        return []


def write_json(data):
    file = open('data.json', mode='w')
    json.dump(data, file)
    file.close()


if __name__ == '__main__':

    with JSONData() as data:
        klient = {'imie': 'Antoni', 'numer_telefonu': 123123123}
        data.append(klient)

        write_json(data)
