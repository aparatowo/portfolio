# Rafał Nitychoruk

GRACZE = ({'imie': 'Celina', 'wygrane': 0, 'przegrane': 0},
          {'imie': 'Barnaba', 'wygrane': 0, 'przegrane': 0},
          {'imie': 'Danuta', 'wygrane': 0, 'przegrane': 0},
          {'imie': 'Alojzy', 'wygrane': 0, 'przegrane': 0})

# tutaj napisz brakującą funkcję
def rozegraj_gre(gracz_jeden, gracz_dwa):
    try:
        if GRACZE[gracz_jeden] and GRACZE[gracz_dwa]:
            GRACZE[gracz_jeden]['wygrane'] = GRACZE[gracz_jeden]['wygrane'] + 1
            GRACZE[gracz_dwa]['przegrane'] = GRACZE[gracz_dwa]['przegrane'] + 1
    except IndexError:
        print('Nie ma gracza o podanym id')

if __name__ == '__main__':
    print(GRACZE)

    rozegraj_gre(1, 2)
    rozegraj_gre(2, 3)
    rozegraj_gre(2, 0)
    rozegraj_gre(3, 0)
    rozegraj_gre(100, 0)
    rozegraj_gre(0, 100)

    print(GRACZE)
