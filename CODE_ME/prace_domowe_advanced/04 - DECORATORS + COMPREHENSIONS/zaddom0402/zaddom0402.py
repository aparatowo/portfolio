# tutaj wpisz swoje imię i nazwisko

def generate_email_addresses(people, email_host):
    final_dict = {}
    for user in people:
        if user['active']:
            user_mail = user['imie'][0].lower() + \
                        user['nazwisko'].lower() + \
                        '@' + email_host
            conversion_dict = {'ą': 'a', 'ć': 'c', 'ę': 'e', 'ł': 'l',
                               'ń': 'n', 'ó': 'o', 'ś': 's', 'ź': 'z', 'ż': 'z'}

            for key, value in conversion_dict.items():
                user_mail = user_mail.replace(key, value)
            final_dict[user['id']] = user_mail

    return final_dict


if __name__ == '__main__':
    people = [
        {'id': 74, 'imie': 'Paulina', 'nazwisko': 'Sobczak', 'active': True},
        {'id': 51, 'imie': 'Henryk', 'nazwisko': 'Bąk', 'active': False},
        {'id': 23, 'imie': 'Kazimierz', 'nazwisko': 'Górski', 'active': True},
        {'id': 32, 'imie': 'Irena', 'nazwisko': 'Wójcik', 'active': True},
        {'id': 60, 'imie': 'Ewa', 'nazwisko': 'Dudziak', 'active': True},
        {'id': 72, 'imie': 'Jakub', 'nazwisko': 'Malinowski', 'active': True},
        {'id': 80, 'imie': 'Jadwiga', 'nazwisko': 'Brzezińska', 'active': False},
        {'id': 91, 'imie': 'Roman', 'nazwisko': 'Sawicki', 'active': True},
        {'id': 10, 'imie': 'Marcin', 'nazwisko': 'Szymczak', 'active': False}
    ]

    adresses = generate_email_addresses(people, 'uczelnia.pl')
    print(adresses)
