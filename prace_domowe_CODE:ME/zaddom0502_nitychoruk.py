# Rafał Nitychoruk
import string

tekst = '''Stoi na stacji lokomotywa,
Ciężka, ogromna i pot z niej spływa:
Tłusta oliwa.

Stoi i sapie, dyszy i dmucha,
Żar z rozgrzanego jej brzucha bucha:
Buch - jak gorąco!
Uch - jak gorąco!
Puff - jak gorąco!
Uff - jak gorąco!
Już ledwo sapie, już ledwo zipie,
A jeszcze palacz węgiel w nią sypie.

Wagony do niej podoczepiali
Wielkie i ciężkie, z żelaza, stali,
I pełno ludzi w każdym wagonie,
A w jednym krowy, a w drugim konie,
A w trzecim siedzą same grubasy,
Siedzą i jedzą tłuste kiełbasy,
A czwarty wagon pełen bananów,
A w piątym stoi sześć fortepianów,
W szóstym armata - o! jaka wielka!
Pod każdym kołem żelazna belka!
W siódmym dębowe stoły i szafy,
W ósmym słoń, niedźwiedź i dwie żyrafy,
W dziewiątym - same tuczone świnie,
W dziesiątym - kufry, paki i skrzynie,
A tych wagonów jest ze czterdzieści,
Sam nie wiem, co się w nich jeszcze mieści.
Lecz choćby przyszło tysiąc atletów
I każdy zjadłby tysiąc kotletów,
I każdy nie wiem jak się wytężał,
To nie udźwigną, taki to ciężar.
Nagle - gwizd!
Nagle - świst!
Para - buch!
Koła - w ruch!'''

# Rozszerzenie
for znak_inter in string.punctuation:
    tekst = tekst.replace(znak_inter, '')

# Punkt 1 i punkt 2
lista_slow = []
for slowo in tekst.split():
    lista_slow.append(slowo.lower())

# Punkt 4a
uzyte_slowa = set()
for slowo in lista_slow:
    uzyte_slowa.add(slowo)

# Punkt 5
lista_posortowana = sorted(uzyte_slowa)

# Punkt 6a
jednolity_string = ' '.join(lista_posortowana)

dlugosc_tekstu = len(lista_slow)  # Punkt 3a
liczba_unikalnych_slow = len(uzyte_slowa)  # Punkt 4b

# Szablony komunikatów
liczba_slow = 'Tekst liczy {} słów'.format(dlugosc_tekstu)
unikalne_slowa = 'Tekst liczy {} unikalnych słów'.format(liczba_unikalnych_slow)

print(lista_slow)
# print(uzyte_slowa)
# print(lista_posortowana)

print(liczba_slow)  # Punkt 3b
print(unikalne_slowa)  # Punkt 4c
print(jednolity_string)  # Punkt 6b
print(lista_posortowana[0], lista_posortowana[-1])  # Punkt 7
