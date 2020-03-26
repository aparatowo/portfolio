# Rafał Nitychoruk

muzyk = {}
muzyk['imie'] = input('Podaj imię i nazwisko muzyka: ')
muzyk['instrument'] = input('Podaj instrument na jakim gra: ')
muzyk['liczba albumów'] = int(input('Podaj liczbę albumów nagranych przez muzyka: '))
muzyk['aktywnosc'] = None

while muzyk['aktywnosc'] == None:
    aktywnosc_muzyka_petla = input('Czy muzyk jest jeszcze aktywny? Podaj odpowiedź (t)ak/(n)ie: ')
    aktywnosc_muzyka_petla = aktywnosc_muzyka_petla.lower()
    if aktywnosc_muzyka_petla == 't' or aktywnosc_muzyka_petla == 'tak':
        muzyk['aktywnosc'] = True
    elif aktywnosc_muzyka_petla == 'n' or aktywnosc_muzyka_petla == 'nie':
        muzyk['aktywnosc'] = False

if muzyk['aktywnosc']:
    print_aktywnosci_muzyka = '\nMuzyk jest aktywny.'
else:
    print_aktywnosci_muzyka = '\nMuzyk nie jest aktywny.'

print(muzyk)
print()

podsumowanie = '{imie} nagrał nagrał(a) {liczba_albumow} albumów.\nJego/jej instrument to {instrument}.{aktywnosc}'.format(
    imie=muzyk['imie'],
    liczba_albumow=muzyk['liczba albumów'],
    instrument=muzyk['instrument'],
    aktywnosc=print_aktywnosci_muzyka
)

print(podsumowanie)
