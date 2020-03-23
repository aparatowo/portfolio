# Zadanie domowe 0301

Uwaga: do rozwiązania każdego zadania musi zostać użyta **co najmniej jedna** lista składana (list comprehension), ale nie trzeba umieszczać całego rozwiązania w jednej liście składanej.

## Etap 1
Napisz funkcję `strip_extensions()`, która przyjmuje listę nazw plików wraz z rozszerzeniami i zwraca listę nazw bez rozszerzeń. Przyjmujemy, że rozszerzeniem nazywamy string, który następuje po pierwszej kropce w nazwie pliku. Zwróć uwagę na to, że:
- przekazany plik może nie mieć rozszerzenia,
- plik może mieć rozszerzenie, które samo w sobie zawiera kropkę
- niewczytany plik widnieje na liście jako `None`, należy go pominąć przy tworzeniu listy wynikowej


## Etap 2
Napisz funkcję `number_of_digits()`, która przyjmuje listę liczb naturalnych (`int`) i zwraca listę krotek (tuple), gdzie:
- pierwszy element krotki jest tą samą liczbą,
- drugi element jest liczbą cyfr, z której składa się dana liczba

### Przykład:
```
[12, 222, -3] -> [(12, 2), (222, 3), (-3, 1)]
```
