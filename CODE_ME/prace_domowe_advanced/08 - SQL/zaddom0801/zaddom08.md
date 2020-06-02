# Zadanie domowe 08

## Wprowadzenie
Zadanie przedstawia prosty symulator plecaka harcerza. Plik `zaddom08_db_init.py` tworzy bazę danych i zapełnia ją przykładowymi danymi.

Zwróć uwagę na definicję kolumny `type`, tabeli `backpack`, która dopuszcza tylko dwie wartości: `equipment` albo `food`.

Plik `zaddom08_db_init.py` nie powinien być modyfikowany.

## Etap 1 - dodawanie przedmiotów do plecaka
Na bazie szablonu stwórz plik `zaddom08_add.py` i zmodyfikuj go tak, aby po udzieleniu odpowiedzi na cztery pytania, został dodany do bazy opisany przedmiot.

Dodaj do funkcji `read_new_item` kod, który umożliwi wybranie typu sprzętu poprzez podanie całego wyrazu lub tylko pierwszej litery nazwy typu. Funkcja zawsze zwraca pełną nazwę typu przedmiotu. W przypadku podania błędych danych rzucony ma zostać wyjątek `ValueError` i cały program ma przerwać działanie.

Dodaj do funkcji `add_items` zapytanie SQL dodające przedmiot o przekazanych cechach do tabeli `backpack` w bazie danych i wywołaj to zapytanie. UWAGA! commit wykonywany jest poniżej w bloku `if __name__ ...`.

## Etap 2 - wypisanie zawartości plecaka
Na bazie szablonu stwórz plik `zaddom08_info.py` i uzupełnij w nim poniższe funkcje:

Funkcja `print_equipment` ma drukować na ekran sprzęty w plecaku, w kolejności alfabetycznej, jeden pod drugim.

Funkcja `print_food` ma drukować na ekran prowiant w plecaku, w kolejności alfabetycznej, jeden pod drugim.

Funkcja `print_backpack_weight` ma drukować na ekran zsumowaną wagę wszystkich przedmiotów w plecaku. UWAGA! Weź pod uwagę nie tylko wagę jednej sztuki przedmiotu, ale także ilość tych przedmiotów w plecaku.

Poniżej przykładowy ekran, po uruchomieniu skryptu z niezmodyfikowanymi danymi w bazie danych:
```
Sprzęt:
Latarka czołowa
Skarpety
Szczoteczka do zębów

Jedzenie:
Wafelek czekoladowy

Waga zawartości: 1.44kg
```
