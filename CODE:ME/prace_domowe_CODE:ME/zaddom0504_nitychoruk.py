# Rafał Nitychoruk

osoby = [{'id': 0, 'imie': 'Paulina', 'nazwisko': 'Sobczak', 'aktywna': True},
         {'id': 5, 'imie': 'Henryk', 'nazwisko': 'Bąk', 'aktywna': False},
         {'id': 11, 'imie': 'Kazimierz', 'nazwisko': 'Górski', 'aktywna': True},
         {'id': 3, 'imie': 'Irena', 'nazwisko': 'Wójcik', 'aktywna': True},
         {'id': 30, 'imie': 'Władysław', 'nazwisko': 'Piotrowski', 'aktywna': False}]

# tutaj wpisz swój kod
print()

print('Aktywni:')
for osoba in osoby:
    if osoba['aktywna'] == True:
        print(osoba['imie'])

print()

print('Nieaktywni:')
for osoba in osoby:
    if osoba['aktywna'] == False:
        print(osoba['imie'])


