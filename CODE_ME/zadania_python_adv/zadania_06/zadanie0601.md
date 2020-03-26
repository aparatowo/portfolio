# Zadanie 06 - 01

Szablon dla tego zadania znajdziesz w katalogu `zadanie0601`

Napisz aplikację internetową: kalkulator mnożący dwie liczby. Aplikacja musi spełniać poniższe kryteria:

1. Pod ścieżką `/` (root) użytkownik ma znaleźć stronę html z formularzem, w którym będzie można podać dwie liczby naturalne (znajdź odpowiedni typ dla elementu `input`). 
    - Każda liczba powinna dostać swoje osobne pole. 
    - HTML dla formularza ma się znaleźć w szablonie `templates/input.html`.
    - Formularz ma przekierować użytkownika do ścieżki `/result`
    - Metoda, jaką formularz wyśle dane, jest dowolna
    
2. Pod ścieżką `/result` użytkownik ma znaleźć wynik mnożenia dwóch liczb, które wcześniej wprowadził.
    - Strona ma zaprezentować wynik w postaci działania, np: 3 * 4 = 12
    - HTML dla tej ścieżki ma znaleźć się w szablonie `templates/result.html`.
    - Jeśli w zapytaniu nie zostaną przekazane poprawne dane, strona ma o tym poinformować zamiast prezentować błędy.
    - Na stronie powinien znaleźć się link umożliwiający powrót do głównej strony (`/`)
    
## Rozszerzenie (dla chętnych)
- Dołącz do kalkulatora zapisywanie historii zapytań. Historia ma być prezentowana na stronie głównej (`/`). Historia ma być przechowywana w zmiennej w aplikacji (nie potrzebujemy trwałości danych).
- W przypadku historii dłuższej niż pięć zapytań, należy wyświetlić tylko pięć ostatnich.
