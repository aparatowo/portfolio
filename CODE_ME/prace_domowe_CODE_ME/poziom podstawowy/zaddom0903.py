# Rafał Nitychoruk
from zaddom0903_gra import podsumowanie_gry, podsumowanie_gracza

GRACZE = ({'imie': 'Celina', 'wygrane': 0, 'przegrane': 2},
          {'imie': 'Barnaba', 'wygrane': 1, 'przegrane': 0},
          {'imie': 'Danuta', 'wygrane': 2, 'przegrane': 1},
          {'imie': 'Alojzy', 'wygrane': 1, 'przegrane': 1},
          {'imie': 'Nowy_gracz', 'wygrane': 0, 'przegrane': 0})

if __name__ == '__main__':
    # etap 1
    podsumowanie_gracza(0, GRACZE)
    podsumowanie_gracza(1, GRACZE)
    print()
    # etap 2
    podsumowanie_gry(GRACZE)
