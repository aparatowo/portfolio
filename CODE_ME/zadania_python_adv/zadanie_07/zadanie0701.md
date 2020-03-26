# Zadanie 07 - 01

- Napisz szablon `zadanie0701_template.html`, dzięki któremu można będzie wyrenderować gazetkę z produktami w promocji. Tylko ten plik należy modyfikować.
- W tym zadaniu **nie piszemy** aplikacji internetowej.
- Użyj skryptu `zadanie0701.py`, aby wyrenderować na podstawie powyższego szablonu kod html, który zapisany zostanie go do pliku `zadanie0701.html`.
- W gazetce widoczne są tylko produkty objęte promocją.
- Nie wolno modyfikować listy `items`.
- Cena produktu musi zawierać walutę i jednostkę.
- Gotowa gazetka jest do obejrzenia w pliku `zadanie0701_przyklad.html`.



### Uwagi:
- Krótki opis składni tabeli w html: https://www.w3schools.com/html/html_tables.asp 
- Jeśli po wyrenderowaniu szablonu widzisz w przeglądarce dziwne znaki, najprawdopodobniej plik szablonu został wczytany ze złym kodowaniem. Aby to naprawić, dodaj w wywołaniu funkcji `open` parametr `encoding` ustawiony na `windows-1250` lub `utf-8` w zależności od tego z jakim kodowaniem stworzony został plik szablonu.
