# Rafał Nitychoruk

def podsumowanie_gracza(gracz_id, baza_graczy):
    imie_gracza = baza_graczy[gracz_id]['imie']
    liczba_wygranych = baza_graczy[gracz_id]['wygrane']
    liczba_przegranych = baza_graczy[gracz_id]['przegrane']
    liczba_rozegranych = liczba_wygranych + liczba_przegranych

    try:
        procent_wygranych = 100 * liczba_wygranych / liczba_rozegranych
    except ZeroDivisionError:
        procent_wygranych = None

    if procent_wygranych == None:
        podsumowanie_gracza = 'Gracz {} nie rozegrał jeszcze ani jednej gry.'.format(imie_gracza)
    else:
        podsumowanie_gracza = 'Gracz {} wygrał {} gier, co stanowi {}% rozegranych gier.' \
            .format(imie_gracza, liczba_wygranych, procent_wygranych)

    print(podsumowanie_gracza)


def podsumowanie_gry(baza_graczy):
    dlugosc_listy_graczy = len(baza_graczy)
    for index_gr in range(dlugosc_listy_graczy):
        podsumowanie_gracza(index_gr, baza_graczy)


