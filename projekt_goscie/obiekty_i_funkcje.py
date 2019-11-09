from math import ceil


class Gosc:
    def __init__(self, strona, im_nazw, towarzysz=False, prosba_tak=False, prosba_nie=False, dzieci=False,
                 os_starsza=False):
        self.strona = strona
        self.nazwisko = im_nazw
        self.towarzysz = towarzysz
        self.prosba_tak = prosba_tak
        self.prosba_nie = prosba_nie
        self.dzieci = dzieci
        self.os_starsza = os_starsza

    def slownik(self):
        return {
            'strona': self.strona,
            'imie i nazwisko': self.nazwisko,
            'osoba towarzyszaca': self.towarzysz,
            'prosba tak': self.prosba_tak,
            'prosba nie': self.prosba_nie,
            'dzieci': self.dzieci,
            'osoba_starsza': self.os_starsza
        }

    def __str__(self):
        return f'Gość: {self.nazwisko}, osoba towarzysząca: {self.towarzysz},' \
               f' dzieci: {self.dzieci}, prośby: {self.prosba_tak} i {self.prosba_nie}.'

    def __repr__(self):
        return f'Gość {self.nazwisko}'


class Stol:
    def __init__(self, liczba_miejsc, gosc=[]):
        self.liczba_miejsc = liczba_miejsc
        self.lista_stol = gosc

    def dodaj_goscia(self, nowy_gosc):
        self.lista_stol.append(nowy_gosc)

    def czy_dodac(self, gosc):
        if len(self.lista_stol) < self.liczba_miejsc:
            for g in self.lista_stol:
                if g.prosba_nie:
                    if gosc.nazwisko in g.prosba_nie:
                        return False
            return True
        else:
            return False

    def lista_slownikow_gosci(self):
        lista_gosci = []
        for g in self.lista_stol:
            lista_gosci.append(g.slownik())
        return lista_gosci

    def __repr__(self):
        return f'Stół o składzie gości: {self.lista_stol}'

def wybor_singla(lista_zrodlowa):
    starsi = []
    single = []
    pary = []
    for g in lista_zrodlowa:
        if g.towarzysz == False and g.os_starsza != True:
            single.append(g)
        elif g.towarzysz == False and g.os_starsza == True:
            starsi.append(g)
        else:
            pary.append(g)
    return starsi, single, pary

def ile_dzieci(lista_zrodlowa):
    liczba_dzieci = 0
    for g in lista_zrodlowa:
        if g.dzieci:
            liczba_dzieci += g.dzieci
    return liczba_dzieci


def podliczenie_gosci(wskazana_lista):
    podlicznie = 0
    for gwl in wskazana_lista:
        podlicznie += 1
        if gwl.towarzysz:
            podlicznie += 1
        if gwl.dzieci:
            podlicznie += gwl.dzieci
    return podlicznie


def wybor_do_stolu(lista_bazowa, miejsc_przy_stole):
    potrzebne_stoly = ceil(podliczenie_gosci(lista_bazowa) / miejsc_przy_stole)
    lista_stolow = []
    for _ in range(potrzebne_stoly + 1):
        lista_stolow.append(Stol(miejsc_przy_stole))

    for g in lista_bazowa:
        for s in lista_stolow:
            if s.czy_dodac(g):
                s.dodaj_goscia(g)
                break

    return lista_stolow

def stoly_do_listy(zadana_lista_stolow):
    ostateczna_lista_stolow = []
    for s in zadana_lista_stolow:
        ostateczna_lista_stolow.append(s.lista_slownikow_gosci())
    return ostateczna_lista_stolow
