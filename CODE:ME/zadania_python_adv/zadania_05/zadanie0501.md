# Zadanie 0501

Napisz aplikację internetową, która będzie zapisywać do pliku i odczytywać z niego jedną informację tekstową. Jako szablonu użyj pliku `zadanie0501_rozwiazanie.py`.

Aplikacja ma spełniać poniższe wymogi:
1. Aplikacja ma obsługiwać ścieżkę `/zapis/data`, gdzie `data` oznaczają dowolny ciąg znaków, który ma zostać zapisany.
    - dane mają być zapisane do pliku `database.txt`
    - w przypadku poprawnego zapisania danych do pliku, na ekranie ma pojawić się komunikat: `Zapisano do bazy dane: "zapisane_dane"`
    - kolejne zapytania pod ten endpoint mają nadpisywać dane w pliku `database.txt` 
2. Aplikacja ma obsługiwać ścieżkę `/odczyt`, pod którą:
    - jeśli plik `database.txt` istnieje, wypisze na ekran komunikat: `Dane w bazie to: "zapisane_dane"` 
    - jeśli plik `database.txt` nie istnieje, wypisze na ekran komunikat: `Najpierw zapisz coś do bazy!` 
