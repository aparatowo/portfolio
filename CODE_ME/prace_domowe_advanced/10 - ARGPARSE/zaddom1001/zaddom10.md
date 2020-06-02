# Zadanie domowe 10

## Wstęp
Na podstawie pliku `zaddom10_szablon.py` stwórz plik `zaddom10.py`, do którego będzie można przekazywać parametry z linii poleceń.
Większość logiki programu `zaddom10.py` znajduje się w plikach `zaddom10_functions.py` oraz `zaddom10_logger.py` których **nie należy modyfikować**.

# Etap 1
W tym etapie umożliwimy użytkownikowi ustawianie poziomu logowania z linii poleceń. 
Przykładowo, uruchomienie programu poleceniem `python zaddom08.py --log-level DEBUG` powinno ustawić poziom logowania na `logging.DEBUG`.

Dodaj opcjonalny parametr `--log-level`, który:
- będzie przyjmował dokładnie jeden argument z linii poleceń
- będzie miał odpowiadającą mu krótką wersję `-v`  (`-l` jest zarezerwowane dla etapu 3)
- będzie miał opis informujący o swoim działaniu
- w przypadku uruchomienia programu bez tego parametru, program ma ustawić poziom logowania na `logging.WARNING`. (Aby uzyskać to działanie, dodając parametr skorzystaj z argumentu `default`)
- UWAGA! nazwa atrybutu nie może mieć w sobie myślnika, więc `argparse` argumentowi `log-level` z linii poleceń przyporządkuje atrybut `log_level`.

Gdy upewnisz się, że powyższe kroki są spełnione:
- Zmodyfikuj argument `--log-level` tak, aby dało się podać tylko argument spośród obsługiwanych opcji (Wszystkie wbudowane poziomy logowania można znaleźć pod `logging._nameToLevel`).

# Etap 2
W tym etapie umożliwimy użytkownikowi podać plik, którego zawartość ma być przeanalizowana. 
Przykładowo, uruchomienie programu poleceniem `python zaddom08 zen.txt` powinno uruchomić program z poziomem logowania `logging.WARNING` i przeanalizować plik o nazwie `zen.txt`.

- Dodaj parametr pozycyjny `filename`.
- Podanie parametru powinno być wymagane do działania programu.
- Parametr ten ma mieć opis informujący o jego działaniu.

# Etap 3 (dla chętnych)
UNIXowy program `wc` ma również kilka innych flag, takich jak:
- `-l`, która powoduje, że wypisana jest tylko liczba linii
- `-w`, która powoduje, że wypisana jest tylko liczba słów
- `-c`, która powoduje, że wypisana jest tylko liczba bajtów

Dodaj te argumenty opcjonalne biorąc pod uwagę, że w naszym programie (w przeciwieństwie do oryginału) argumenty te wykluczają się wzajemnie. Podpowiedź: https://stackoverflow.com/questions/11154946/require-either-of-two-arguments-using-argparse

