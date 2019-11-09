from przetwarzanie_list_gosci import lista_gosci, lista_single, lista_starsi, lista_pary
from obiekty_i_funkcje import ile_dzieci, podliczenie_gosci, wybor_do_stolu, stoly_do_listy
from math import ceil
import random
import json

if __name__ == '__main__':
    liczba_miejsc_przy_stole = 8
    dzieci = ile_dzieci(lista_gosci)
    stoly_dla_dzieci = ceil(dzieci / liczba_miejsc_przy_stole)
    liczba_gosci = podliczenie_gosci(lista_gosci)
    lista_losowan = []

    for _ in range(1000):
        zadowolenie = 0
        random.shuffle(lista_pary)
        random.shuffle(lista_starsi)
        random.shuffle(lista_single)
        stoly_par = wybor_do_stolu(lista_pary, liczba_miejsc_przy_stole / 2)
        stoly_singli = wybor_do_stolu(lista_single + lista_starsi, liczba_miejsc_przy_stole)

        for s in stoly_par:
            for g in s.lista_stol:
                if g.prosba_tak:
                    if g.nazwisko in g.prosba_tak:
                        zadowolenie += 1
        lista_losowan.append({'zadowolenie': zadowolenie, 'stoly par': stoly_par, 'stoly singli': stoly_singli})

    optymalne_listy_par = []
    optymalne_listy_singli = []
    ocena_zadowolenia = max([d['zadowolenie'] for d in lista_losowan])
    for d in lista_losowan:
        if int(d['zadowolenie']) == ocena_zadowolenia:
            optymalne_listy_par.append(d['stoly par'])
            optymalne_listy_singli.append(d['stoly singli'])
            break

    stoly_par = random.choice(optymalne_listy_par)
    stoly_singli = random.choice(optymalne_listy_singli)
    export_danych = {'stoly par': stoly_do_listy(stoly_par),
                     'stoly singli i osob starszych': stoly_do_listy(stoly_singli),
                     'stoly dla dzieci': stoly_dla_dzieci}

    for stolik in stoly_par:
        index_stolika = stoly_par.index(stolik)
        print()
        szablon = f'Stół numer {index_stolika + 1}'
        print(szablon.center(70, '-'))
        print(f'Przy stole siedzi {len(stolik.lista_stol)} par, czyli łącznie {len(stolik.lista_stol) * 2} osób.')
        for gosc in stolik.lista_stol:
            print(gosc)

    for stolik in stoly_singli:
        index_stolika = stoly_singli.index(stolik)
        print()
        szablon= f'Stół numer {index_stolika + 1}'
        print(szablon.center(70, '_'))
        print(f'Przy stole siedzi {len(stolik.lista_stol)} osób.')
        for gosc in stolik.lista_stol:
            print(gosc)

    print(f'')
    print(f'Niezbędnych będzie {stoly_dla_dzieci} stołów dla {dzieci} dzieci.')


    nazwa_pliku = input('Podaj nazwę pliku do zapisu: ')

    with open(f'{nazwa_pliku}.json', mode='w', encoding='utf-8') as plik:
        plik.write(json.dumps(export_danych))
