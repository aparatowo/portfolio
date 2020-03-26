# Zadanie domowe 0601

W tym zadaniu należy na podstawie szablonu aplikacji dostępnego w tym katalogu stworzyć własną aplikację, która będzie umożliwiała dodawanie z formularza kolejnych liczb do bazy danych (w pliku JSON). Aplikacja będzie umożliwiać również wyświetlenie danych w bazie.

Aplikacja ma spełniać poniższe założenia:
- Plik `database.json` przechowuje listę zgodną z formatem JSON. (Uwaga techniczna: W przypadku zapisania do tego pliku niepoprawnych wartości należy ręcznie zastąpić jego zawartość pustą listą `[]`. Programistyczna obsługa powyższej sytuacji jest rozszerzeniem tego zadania.)

- Aplikacja będzie posiadać trzy endpointy:
    - `\ ` (root), obsługuje tylko metodę GET. Zwraca szablon `index.html` wypełniony liczbą wprowadzonych do bazy liczb.
    - `\add`, obsługuje tylko metodę POST. Służy do zapisania liczby wprowadzonej w formularzu do bazy danych. Zwraca tekst "Liczba (tutaj przekazana liczba) dodana!"
    - `\numbers`, obsługuje tylko metodę GET. Zwraca tekst w formacie JSON przedstawiający listę liczb wpisanych do bazy danych
        - Endpoint przyjmuje jeden parametr ("query parameter") `order`. Jeśli ten parametr ustawiony jest na `asc`, lista powinna być posortowana rosnąco. Jeśli parametr ustawiony jest na `desc`, lista powinna być posortowana malejąco.
        - Jeśli parametr `order` jest ustawiony na inną wartość lub nie jest ustawiony, endpoint zwraca listę liczb w kolejności w jakiej były wprowadzane.

- Szablon `index.html` należy rozszerzyć o poniższe elementy:
    - należy stworzyć formularz, który umożliwi wprowadzenie jednej liczby i wysłanie danych metodą POST do endpointu `\add`
    - należy wyświetlić w "Liczba wpisanych liczb w bazie: (tutaj wyliczona liczba)" aktualną liczbę wpisanych do bazy liczb.
    - należy uzupełnić parametr `href` w hiperlinkach "rosnąco" i "malejąco" tak, aby kliknięcie na nie przenosiło użytkownika do strony `\numbers` z wynikiem posortowanym odpowiednio rosnąco i malejąco. 

## Rozszerzenie:
Dodaj do aplikacji obsługę braku pliku `database.json` oraz złego formatu danych w nim zawartych.
