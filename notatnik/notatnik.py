import datetime


class Notatnik:
    def __init__(self, lista_notatek=[]):
        self.notatki = lista_notatek

    def ilosc_notatek(self):
        return len(self.notatki)

    def listuj_notatki(self):
        print('Oto lista notatek:')
        tytuly_notatek = []
        for n in self.notatki:
            tytuly_notatek.append(['tytul'])
        tytuly_notatek = enumerate(tytuly_notatek, 1)
        for n in tytuly_notatek:
            print(n)

    def nowa_notatka(self, tytul='brak tytułu', tresc='brak opisu', data='brak daty', priorytet=1):
        priorytet = priorytet
        if priorytet is int and priorytet in [1, 2, 3, 4]:
            pass
        else:
            priorytet = 1

        notatka = {'tytul': tytul, 'tresc': tresc, 'data': data, 'data dodania': datetime.datetime,
                   'priorytet': priorytet}
        self.notatki.append(notatka)

    def kasuj_notatke(self, tytul=None):
        if tytul != None:
            for n in self.notatki:
                if tytul in n['tytul']:
                    self.notatki.pop()
                    break
        else:
            self.listuj_notatki()
            tytul_kasuj = input('Wybierz z powyższej listy notatkę do usunięcia, lub podaj "anuluj" aby zrezygnować: ')
            if tytul_kasuj == 'anuluj':
                return
            else:
                for n in self.notatki:
                    if n['tytul'] == tytul_kasuj:
                        self.notatki.pop(n)
                        break

    def wyczysc_notatnik(self):
        decyzja = input(
            'Tego nie da się cofnąć. Jeśli jesteś pewien wpisz "TAK", lub naciśnij dowolny klawisz aby anulować.')

        if decyzja == 'TAK':
            self.notatki = []
            print('Notatnik został wyczyszczony')
        else:
            print('Notatnik nie został wyczyszczony. ')

    def ile_notatek(self):
        return len(self.notatki)

    def __str__(self):
        if len(self.notatki) > 0:
            ilosc_notatek = len(self.notatki)
            szablon = f'Notatnik zawiera: {ilosc_notatek}'
        else:
            szablon = f'Notatnik nie zawiera notatek'
        return szablon
#
# notatka1 = Notatnik()
#
# notatka1.nowa_notatka()
#
# notatka1.listuj_notatki()
# print(f'Lista ma {notatka1.ile_notatek()} notatek')
# notatka1.nowa_notatka('tytul', 'wpis')
# print(notatka1)
# print()
# print('przed usunięciem')
# notatka1.listuj_notatki()
# print(f'Lista ma {notatka1.ile_notatek()} notatek')
# print(notatka1)
# print()
# notatka1.kasuj_notatke('tytul')
# print()
# print('po usunięciu')
# notatka1.listuj_notatki()
# print(f'Lista ma {notatka1.ile_notatek()} notatek')
# print(notatka1)
#
