from random import choice, randint
import pickle
from datetime import datetime
from notatnik import Notatnik


def powitanie():
    print('Cześć! Jak się masz? Jestem gotowy do pracy!\n'
          'Pewnie chcesz poznać moje możliwości?')


def napisz_notatke(wskazany_notatnik):
    wpisano_tytul = False
    wpisano_tresc = False
    wpisano_date = False
    wpisano_priorytet = False

    while wpisano_tytul == False:
        tytul = input('Podaj tytuł: ')
        tytul = tytul.strip()
        if tytul == '':
            wpisano_tytul = 'BRAK TYTUŁU'
        else:
            wpisano_tytul = tytul

    while wpisano_tresc == False:
        tresc = input('Podaj treść notatki:')
        tresc = tresc.strip()
        if tresc == '':
            break
        else:
            wpisano_tresc = tresc

    while wpisano_date == False:
        data = input('Wpisz datę w postaci DD-MM-RRRR:')
        data = data.strip()
        if data == '':
            wpisano_date = datetime
        else:
            wpisano_date = data

    while wpisano_priorytet == False:
        priorytet = input('Podaj priorytet w skali 1-4. Im wyższa liczba całkowita tym ważniejsza notatka.')
        priorytet = priorytet.strip()
        if priorytet == '':
            wpisano_priorytet = '1'
        else:
            wpisano_priorytet = priorytet

    wskazany_notatnik.nowa_notatka(wpisano_tytul, wpisano_tresc, wpisano_date, wpisano_priorytet)

def czytaj_notatke(wskazany_notatnik):
    wskazany_notatnik.listuj_notatki()
    wskazana_notatka = False
    while wskazana_notatka == False:
        numer_notatki = input('Podaj numer notatki, którą chcesz odczytać: ')
        szukany_index = int(numer_notatki) - 1
        if szukany_index <= wskazany_notatnik.ilosc_notatek():
            wskazana_notatka = wskazany_notatnik.notatki[szukany_index]
            print('Tytuł notatki {}', format(wskazana_notatka['tytul']))
            print('Treść notatki {}', format(wskazana_notatka['tresc']))
            print('Data dla notatki {}', format(wskazana_notatka['data']))
            print('Priorytet notatki {}', format(wskazana_notatka['priorytet']))
        elif numer_notatki.strip().lower() == 'wyjdź':
            return
        else:
            print('Nie rozpoznano numeru.')


def utworz_czytaj(wskazany_notatnik):
    wybor = input('Aby utworzyć notatkę wpisz "T".\n'
                  'Aby odczytać notatkę, wpisz "C".\n'
                  'Aby odczytać notatki z pliku, wpisz "O" - uwaga, to nadpisze obecny notatnik.\n'
                  'Aby zapisać notatki do pliku wpisz "Z".\n'
                  'Możesz wyjść z programu wpisując "W".\n'
                  'Pisz tutaj (T/C/O/Z/W): ')

    if wybor.capitalize() == 'T':
        napisz_notatke(wskazany_notatnik)
    elif wybor.capitalize() == 'C':
        czytaj_notatke(wskazany_notatnik)
    elif wybor.capitalize() == 'O':
        otwieranie(wskazany_notatnik)
    elif wybor.capitalize() == 'Z':
        zapisywanie(wskazany_notatnik)

    elif wybor.capitalize() == 'W':
        exit()
    else:
        print('Nie rozumiem, spróbuj ponownie.')

    print()

def otwieranie(wskazany_notatnik):
    wskazany_plik = input(
        "Podaj nazwę pliku. Plik musi znajdować się w katalogu 'users' wewnątrz katalogu z programem.")
    wskazany_plik = wskazany_plik.strip() + ".txt"

    try:
        with open(wskazany_plik, 'rb') as plik:
            wskazany_notatnik.notatki = pickle.loads(plik.read())
    except FileNotFoundError:
        error_happens()
        print(f'Jesteś pewien, że istnieje taki plik jak {wskazany_plik}? Pamiętaj, że program czyta tylko pliki, które sam stworzył.\n'
              'Istotna jest też wielkość liter w nazwie. Może spróbuj jeszcze raz?')

def zapisywanie(wskazany_notatnik):
    wskazany_plik = input(
        "Podaj nazwę pliku. Plik musi znajdować się w katalogu 'users' wewnątrz katalogu z programem.")
    wskazany_plik = wskazany_plik.strip() + ".txt"

    if wskazany_plik == 'dupa.txt':
        its_a_prank_bro()

    wekowany_notatnik = pickle.dumps(wskazany_notatnik.notatki)
    with open(wskazany_plik, 'wb') as plik:
        plik.write(wekowany_notatnik)

def error_happens():
    pick = randint(1, 2)
    if pick == 1:
        print('''
    ▌─────────────────────────▐█─────▐
    ▌────▄──────────────────▄█▓█▌────▐
    ▌───▐██▄───────────────▄▓░░▓▓────▐
    ▌───▐█░██▓────────────▓▓░░░▓▌────▐
    ▌───▐█▌░▓██──────────█▓░░░░▓─────▐
    ▌────▓█▌░░▓█▄███████▄███▓░▓█─────▐
    ▌────▓██▌░▓██░░░░░░░░░░▓█░▓▌─────▐
    ▌─────▓█████░░░░░░░░░░░░▓██──────▐
    ▌─────▓██▓░░░░░░░░░░░░░░░▓█──────▐
    ▌─────▐█▓░░░░░░█▓░░▓█░░░░▓█▌─────▐
    ▌─────▓█▌░▓█▓▓██▓░█▓▓▓▓▓░▓█▌─────▐
    ▌─────▓▓░▓██████▓░▓███▓▓▌░█▓─────▐
    ▌────▐▓▓░█▄▐▓▌█▓░░▓█▐▓▌▄▓░██─────▐
    ▌────▓█▓░▓█▄▄▄█▓░░▓█▄▄▄█▓░██▌────▐
    ▌────▓█▌░▓█████▓░░░▓███▓▀░▓█▓────▐
    ▌───▐▓█░░░▀▓██▀░░░░░─▀▓▀░░▓█▓────▐
    ▌───▓██░░░░░░░░▀▄▄▄▄▀░░░░░░▓▓────▐
    ▌───▓█▌░░░░░░░░░░▐▌░░░░░░░░▓▓▌───▐
    ▌───▓█░░░░░░░░░▄▀▀▀▀▄░░░░░░░█▓───▐
    ▌──▐█▌░░░░░░░░▀░░░░░░▀░░░░░░█▓▌──▐
    ▌──▓█░░░░░░░░░░░░░░░░░░░░░░░██▓──▐
    ▌──▓█░░░░░░░░░░░░░░░░░░░░░░░▓█▓──▐
    ▌──██░░░░░░░░░░░░░░░░░░░░░░░░█▓──▐
    ██████████████████████████████████
    █░▀░░░░▀█▀░░░░░░▀█░░░░░░▀█▀░░░░░▀█
    █░░▐█▌░░█░░░██░░░█░░██░░░█░░░██░░█
    █░░▐█▌░░█░░░██░░░█░░██░░░█░░░██░░█
    █░░▐█▌░░█░░░██░░░█░░░░░░▄█░░▄▄▄▄▄█
    █░░▐█▌░░█░░░██░░░█░░░░████░░░░░░░█
    █░░░█░░░█▄░░░░░░▄█░░░░████▄░░░░░▄█
    ██████████████████████████████████''')
    elif pick == 2:
        print('''
█▀▀▀██▀▀▀▀▀▀██▀▀▀▀▀▀██▀▀▀▀▀▀██▀▀▀▀▀▀█
█───██──────██──────██──────██──────█
█──███──██──██──██──██──██──██──██──█
█───██──────██──────██──██──██──────█
█──███──▄──▄██──▄──▄██──██──██──▄──▄█
█───██──██─███──██─███──────██──██─██
█▄▄▄██▄▄██▄▄██▄▄██▄▄██▄▄▄▄▄▄██▄▄██▄▄█
    ''')

def its_a_prank_bro():
    print('''
─────────▄──────────────▄────
────────▌▒█───────────▄▀▒▌───
────────▌▒▒▀▄───────▄▀▒▒▒▐───
───────▐▄▀▒▒▀▀▀▀▄▄▄▀▒▒▒▒▒▐───
─────▄▄▀▒▒▒▒▒▒▒▒▒▒▒█▒▒▄█▒▐───
───▄▀▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▀██▀▒▌───
──▐▒▒▒▄▄▄▒▒▒▒▒▒▒▒▒▒▒▒▒▀▄▒▒▌──
──▌▒▒▐▄█▀▒▒▒▒▄▀█▄▒▒▒▒▒▒▒█▒▐──
─▐▒▒▒▒▒▒▒▒▒▒▒▌██▀▒▒▒▒▒▒▒▒▀▄▌─
─▌▒▀▄██▄▒▒▒▒▒▒▒▒▒▒▒░░░░▒▒▒▒▌─
─▌▀▐▄█▄█▌▄▒▀▒▒▒▒▒▒░░░░░░▒▒▒▐─
▐▒▀▐▀▐▀▒▒▄▄▒▄▒▒▒▒▒░░░░░░▒▒▒▒▌
▐▒▒▒▀▀▄▄▒▒▒▄▒▒▒▒▒▒░░░░░░▒▒▒▐─
─▌▒▒▒▒▒▒▀▀▀▒▒▒▒▒▒▒▒░░░░▒▒▒▒▌─
─▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐──
──▀▄▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▄▒▒▒▒▌──
────▀▄▒▒▒▒▒▒▒▒▒▒▄▄▄▀▒▒▒▒▄▀───
───▐▀▒▀▄▄▄▄▄▄▀▀▀▒▒▒▒▒▄▄▀─────
──▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▀▀────────
──     W s z y s t k o    ───
──   w i d z i a ł e m !  ───
─────   D   U   P   A   ─────
─────   Z  B  I  T  A   ─────
─────     A   L   E     ─────
─────  Z A P I S A N A  ─────
''')