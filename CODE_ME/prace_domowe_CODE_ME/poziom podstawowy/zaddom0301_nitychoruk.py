# Rafał Nitychoruk

imiona = ['Czesław', 'Barbara', 'Jadwiga', 'Zenon', 'Artur']
print(imiona)
nowe_imie = input('Proszę podać nowe imię: ')

# tutaj wpisz swój kod
if nowe_imie in imiona:
    print('To imię jest już na liście.')
elif len(nowe_imie) >= 2:
    imiona.append(nowe_imie)
else:
    print("Imię musi mieć minimum dwa znaki. 'Jo' przejdzie, spacja nie.")

dlugosc_listy_imiona = len(imiona)
print('Na liście znajduje się',dlugosc_listy_imiona, 'imion.')

posortowane_imiona = sorted(imiona)

for imie_na_liscie in posortowane_imiona:
    print(imie_na_liscie)

print('Koniec programu.')
