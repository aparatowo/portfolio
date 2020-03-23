# Zadanie domowe 07

Zapoznaj się z aplikacją `zaddom07.py`. W tym stanie aplikacja pokazuje tylko strony z przykładowymi danymi.

W katalogu `templates_przyklady` znajdują się wygenerowane pliki html, które pokazują jak mają wyglądać strony dla poszczególnych widoków:
- `lista.html` zawiera listę wszystkich osób w bazie
- `osoba.html` pokazuje jak wygląda "wizytówka" konkretnej osoby
- `osoba_admin.html` pokazuje jak wygląda "wizytówka" konkretnej osoby, która jest adminem
- `osoba_err.html` pokazuje jak wygląda ta sama strona, gdy użytkownik poda 'id', którego nie ma w bazie

Pliki w katalogu `templates` są wykorzystywane przez aplikacje i aby ukończyć zadanie, należy je zmodyfikować.

## Zadanie

1. Napisz szablon, dzięki któremu pod ścieżką `/` wyświetlona zostanie lista wszystkich osób z bazy.
    - Jeśli dana osoba jest adminem, po prawej stronie linka ma pojawić się pogrubiony napis "[ADMIN]"
    - Imie każdej osoby ma na liście być prezentowane jako inicjał (http://jinja.pocoo.org/docs/2.10/templates/#builtin-filters)
2. Zaprogramuj endpoint `osoba()` i napisz odpowiednie szablony tak, aby dla ścieżki `/osoba/id` renderowana była strona html, na której:
    - Zaprezentowane są dane osoby, która jest w bazie pod indeksem `id`
    - Dane zaprezentowane są w taki sposób, jak widać to w przykładowym pliku `osoba.html` lub `osoba_admin.html`. Oznacza to, że osoba, która jest adminem, ma dodatkową pozycję w tabeli.
    - Jeśli podane zostanie `id`, którego nie ma w bazie, ma zostać zaprezentowana strona wyglądająca jak `osoba_err.html`.
    
## WAŻNE OGRANICZENIE:

Wynik zaprezentowany pod ścieżką `/osoba/id` zawiera style. Jako, że chcemy zachować spójność naszej strony, nie dopuszczam kopiowania i wklejania styli między plikami. Oznacza to, że obsługę trzech różnych wyników (osoba "zwykła", admin, brak osoby) należy rozwiązać na jeden z poniższych sposobów:
1. Stworzenie jednego szablonu `osoba.html`, który odpowiednio renderuje stronę używając bloków `if`. (DOMYŚLNE)
2. Stworzenie kilku szablonów, które dziedziczą menu i styl po jednym bazowym szablonie. (TRUDNE)
3. Stworzenie kilku szablonów które korzystają ze styli z jednego zewnętrznego pliku CSS (POZA ZAKRESEM NASZYCH ZAJĘĆ)
