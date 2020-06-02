# Zadanie 1401

Plik `zaddom1401.py` zawiera dane użytkowników `data`, które należy posortować po dacie ich dołączenia do serwisu (`join_date`). Wartość parametru `key` funkcji `sorted` jest wyliczana przez funkcję `sort_key`.

Napisz tak samo działający kod, wymieniając użycie funkcji `sort_key` na lambdę i zapisz wynik do zmiennej `sorted_by_date_with_lambda`.

## Test
Linijka:
```
assert sorted_by_date == sorted_by_date_with_lambda
```
Wyprodukuje `AssertionError`, gdy obie listy nie będą takie same.