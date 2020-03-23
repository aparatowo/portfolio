# Zadanie domowe 0302

W tym zadaniu należy napisać funkcję, która wyciągnie z pliku `apache_logs` interesujące nas informacje.

Plik `apache_logs`, to plik tekstowy, w którym zapisane jest każde zapytanie, jakie użytkownicy skierowali do pewnego serwera. Jedna linia to jedno zapytanie. Poszczególne informacje dla jednego zapytania oddzielone są spacjami (pewne informacje są zgrupowane za pomocą znaku `"`)

W tym etapie należy napisać funkcję `unique_ip_addresses()`, która otworzy plik `apache_logs` i na podstawie jego zawartości zwróci listę adresów IP, które wysyłały zapytania do naszego serwera. W przypadku wielu zapytań z jednego adresu zapisujemy adres na liście wynikowej tylko raz.

- Adres IP (w wersji 4) zapisywany jest w postaci `x.x.x.x`, gdzie `x` to liczba z zakresu od 0 do 255. 
- Funkcja **musi** zwracać listę stringów, gdzie każdy string to jeden adres IP. 
- Postaraj się nie wczytywać zawartości całego pliku na raz do jednej zmiennej. Takie pliki zwykle są naprawdę duże. 
