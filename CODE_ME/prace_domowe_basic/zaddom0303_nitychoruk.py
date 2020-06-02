# Rafał Nitychoruk

liczba_naturalna = int(input('Podaj liczbę naturalną: '))
lista_dzielnikow = []

for liczba in range(1, liczba_naturalna + 1):
    if liczba_naturalna % liczba == 0:
        print('Podana liczba {} jest podzielna przez {}'.format(liczba_naturalna, liczba))
        lista_dzielnikow.append(liczba)

print('Podana liczba {} jest podzielna przez {}.'.format(liczba_naturalna, lista_dzielnikow))

if len(lista_dzielnikow) == 2:
    print('Podana liczba {} jest liczbą pierwszą.'.format(liczba_naturalna))