# Ta linia testuje program, który napiszesz ;)
# Rafał Nitychoruk

from random import choice
from string import ascii_lowercase, ascii_letters, punctuation


def generuj_haslo(poziom_trudnosci_hasla=0, dlugosc_hasla=8):
    if poziom_trudnosci_hasla == 0:
        dostepne_znaki = ascii_lowercase
    elif poziom_trudnosci_hasla == 1:
        dostepne_znaki = ascii_letters
    elif poziom_trudnosci_hasla == 2:
        dostepne_znaki = ascii_letters + '0123456789'
    elif poziom_trudnosci_hasla == 3:
        dostepne_znaki = ascii_letters + '0123456789' + punctuation

    losowe_znaki = []
    for _ in range(dlugosc_hasla):
        losowy_znak = choice(dostepne_znaki)
        losowe_znaki.append(losowy_znak)

    losowe_haslo = ''
    losowe_haslo = losowe_haslo.join(losowe_znaki)
    # for znak in losowe_znaki:
    #     losowe_haslo = losowe_haslo + znak
    print('Twoje losowe hasło o długości {} znaków to {}.'.format(dlugosc_hasla, losowe_haslo))
    return losowe_haslo

trudnosc = None
ilosc_znakow = None

while trudnosc == None:
    podaj_trudnosc = input('Podaj poziom trudności hasła w skali 0-3: ')
    if podaj_trudnosc == '1' or podaj_trudnosc == '2' or podaj_trudnosc == '3':
        trudnosc = int(podaj_trudnosc)

while ilosc_znakow == None:
    podaj_ilosc_znakow = input('Jak długie ma być hasło? Podaj liczbę całkowitą: ')
    if podaj_ilosc_znakow.isdigit():
        ilosc_znakow = int(podaj_ilosc_znakow)


haslo = generuj_haslo(trudnosc, ilosc_znakow)
print(haslo)