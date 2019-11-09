from obiekty_i_funkcje import Gosc, wybor_singla

plik_goscie_mloda = open(input('Podaj nazwę pliku CSV listą gości Panny Młodej.\nMożesz skorzystać z pliku "lista_gosci.csv"\nPisz tutaj: '), 'r', encoding='UTF-8')
plik_goscie_mlody = open(input('Podaj nazwę pliku CSV listą gości pana Młodego.\nMożesz skorzystać z pliku "lista_gosci2.csv"\nPisz tutaj: '), 'r', encoding='UTF-8')

def rozpakowanie_pliku(wskazany_plik):
    pomijanie_naglowka = wskazany_plik.readline()
    rozpakowana_lista = []
    for linia in wskazany_plik:
        linia_podzielona = linia.split(',')
        strona_line = linia_podzielona[0].strip()
        im_nazw_line = linia_podzielona[1].strip()
        towarzysz_line = linia_podzielona[2].strip()
        prosba_tak_line = linia_podzielona[3].strip()
        prosba_nie_line = linia_podzielona[4].strip()
        dzieci_line = linia_podzielona[5].strip()
        os_starsza_line = linia_podzielona[6].strip()
        if 'nie' in towarzysz_line:
            towarzysz_line = False
        elif towarzysz_line == '':
            towarzysz_line = False
        if 'nie' in prosba_tak_line:
            prosba_tak_line = False
        elif prosba_tak_line == '':
            prosba_tak_line = False
        if 'nie' in prosba_nie_line:
            prosba_nie_line = False
        elif prosba_nie_line == '':
            prosba_nie_line = False
        if dzieci_line.isdigit():
            dzieci_line = int(dzieci_line)
        else:
            dzieci_line = False
        if 'tak' in os_starsza_line:
            os_starsza_line = True
        else:
            os_starsza_line = False
        rozpakowana_lista.append(
            Gosc(strona_line, im_nazw_line, towarzysz_line, prosba_tak_line, prosba_nie_line, dzieci_line,
                 os_starsza_line))
    return rozpakowana_lista


goscie_mloda = rozpakowanie_pliku(plik_goscie_mloda)
goscie_mlody = rozpakowanie_pliku(plik_goscie_mlody)
lista_gosci = goscie_mloda + goscie_mlody
lista_starsi, lista_single, lista_pary = wybor_singla(lista_gosci)
