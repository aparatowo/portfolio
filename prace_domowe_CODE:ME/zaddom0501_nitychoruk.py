# Rafał Nitychoruk

suma = 0
lista = []
# while suma <= 100:
#     wpisano = int(input('Podaj liczbę: '))
#     if wpisano > 0:
#         lista.append(wpisano)
#         print('Teraz wpisano', wpisano)
#         print('W sumie wpisano do tej pory', len(lista), 'poprawnych liczb i są to:', str(lista) + '.\nIch suma to:', sum(lista))
#     else:
#         print('Podaj liczbę dodatnią.')
#     suma = sum(lista)
#
# print('Suma przekroczyła 100. Koniec programu.')

def drukowanie(placeholder_listy):
    for liczba in placeholder_listy[:-1]:
        print(liczba, end='+')
    print(placeholder_listy[-1], end='=')
    print(str(suma))


while suma <= 100:
    wpisano = int(input('Podaj liczbę: '))
    if wpisano > 0 and len(lista) == 0:
        lista.append(wpisano)
        suma = sum(lista)
        print('{} = {}'.format(wpisano, wpisano))
    elif wpisano > 0 and len(lista) > 0:
        lista.append(wpisano)
        suma = sum(lista)
        drukowanie(lista)
    else:
        print('Podaj liczbę dodatnią.')


print('Suma przekroczyła 100. Koniec programu.')
