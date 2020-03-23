# Zadanie Domowe 01

W tym zadaniu należy dokończyć implementację klasy `MyTime`. Klasa ta ma przechowywać czas w minutach i sekundach oraz wspierać podstawowe operacje na tych czasach.

Zadanie podzielone jest na etapy, które najlepiej wykonywać w podanej kolejności.

Aby przetestować, czy dany etap jest rozwiązany poprawnie, można użyć dołączonych do zadania testów. Kilka uwag:
- aby testy działały, należy rozwijać klasę w pliu `zaddom01.py` (stworzonym z szablonu)
- testy można uruchamiać z PyCharma klikając na dany plik prawym klawiszem i wybierając "run"
- aby uruchomić wszystkie testy w katalogu, należy wejść do tego katalogu i z linii poleceń uruchomić `python -m unittest`


## Etap 1
- Napisz metodę `__init__`, która:
    - umożliwia ustawienie dodatniej lub zerowej liczby minut.
    - umożliwia ustawienie liczby sekund z zakresu od 0 do 59.
    - atrybuty klasy, przechowujące powyższe wartości muszą nazywać się `_minutes` oraz `_seconds` (w przeciwnym razie testy nie przejdą)
    - jeśli wprowadzone wartości nie spełniają powyższych warunków skrypt ma zgłosić (`raise`) wyjątek `ValueError`
    
- Napisz metodę `__repr__`, która dany czas przedstawi w poniższym formacie: `MyTime(min=<liczba minut>, sec=<liczba sekund>)`


## Etap 2
- Napisz metody `__lt__` oraz `__eq__`, tak aby można było porównywać, który z dwóch czasów jest krótszy, który dłuższy, oraz czy są równe.
- UWAGA: operator `<=` i `>=` nie jest wymagany


## Etap 3
- Napisz metodę `__add__`, która umożliwi dodawanie dwóch czasów za pomocą operatora `+`.
- Zwróć uwagę na to, że nowy czas jaki otrzymamy po dodaniu dwóch innych nie może mieć liczby sekund większej niż 59.
- dokumentacja: https://docs.python.org/3/reference/datamodel.html#emulating-numeric-types


## Etap 4
- Napisz metodę `__sub__`, która umożliwi odejmowanie dwóch czasów za pomocą operatora `-`.
- Jeśli w wyniku odejmowania otrzymamy ujemną liczbę minut lub sekund, powinien zostać podniesiony wyjątek `ValueError` 
