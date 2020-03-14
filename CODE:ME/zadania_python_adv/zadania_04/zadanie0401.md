# Zadanie 04 - 01

Otwórz plik `zadanie0401_szablon.py`. Jest to prosty skrypt, który odczytuje listę z pliku `data.json`, dopisuje do niej słownik z danymi klienta, a następnie zapisuje zmodyfikowaną listę z powrotem do tego samego pliku.

W tym zadaniu nie ma potrzeby modyfikowania funkcji `read_json()` oraz `write_json()`.

## Etap 1

Napisz context manager `JSONData`, który:
- w metodzie `__enter__()` wczyta listę z pliku `data.json` i zwróci ją jako obiekt.
- będzie posiadał metodę `__exit__()` ale nie będzie ona nic robiła.

Zmodyfikuj kod skryptu w bloku `if...main` tak, aby korzystał z context managera `JSONData` i nie używał wprost funkcji `read_json()`. Zmodyfikowaną listę nadal należy zapisywać wywołując funkcję `write_json()` wprost.

## Etap 2

Zmodyfikuj context manager `JSONData` tak, aby:
- w metodzie `__enter__()` dane z pliku zapisane były najpierw do atrybutu `self._data` a następnie ten atrybut był zwrócony.
- w metodzie `__exit__()` wywołana ma być funkcja `write_json()`, która zapisze do pliku aktualną zawartość obiektu `self._data`.

Jeśli twój context manager działa poprawnie, możesz usunąć z bloku `if-main` użycie funkcji `write_json()`
 
