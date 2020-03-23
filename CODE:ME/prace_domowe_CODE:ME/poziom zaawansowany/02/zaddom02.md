# Zadanie domowe 02

W tym zadaniu stworzymy klasę `Deck`, która zachowaniem będzie przypominała prawdziwą talię kart. Następnie wykorzystamy tę klasę do rozdania kart kilku graczom.

## Etap 01

- Użyj szablonu `zaddom02_e1_szablon.py`, znajdziesz w nim szkielet klasy `Deck`.
- Uzupełnij klasę tak, aby była jednocześnie iterowalna (*iterable*) oraz była iteratorem (*iterator*), czyli:
    - napisz metodę `__iter__`, która zwróci ten sam obiekt, z którego została zawołana.
    - napisz metodę `__next__`, która zwróci losową kartę (string, np. '2♠').
- Tak jak prawdziwa talia, każdą kartę możemy z talii wyciągnąć tylko raz.
- Gdy wyciągniemy z talii ostatnią kartę, już nie możemy wylosować kolejnej.
- Losowość zaimplementuj używając modułu `random` z biblioteki standardowej.
- Testy do tego etapu można znaleźć w pliku `test_zaddom02_e1.py`

## Etap 02

- Użyj szablonu `zaddom02_e2_szablon.py`.
- Napisz funkcję `draw_cards()`, która zwracać będzie **listę** rozdanych kart.
- Jeśli podczas rozdawania skończą się karty w talii, funkcja ma zwrócić tyle kart ile udało się wyciągnąć.
- Jeśli użytkownik nie wpisze ile kart wylosować, ma zostać zwrócona lista jednoelementowa, z jedną kartą. Jeśli użytkownik wpisze 0 lub liczbę ujemną, to funkcja ma zwrócić pustą listę.
- Do parametru `deck` należy przekazywać talię, z której korzystamy w "grze". 

Podpowiedzi i ograniczenia:
- Funkcja ma podczas rozdawania ma "wyciągać z talii po jednej karcie" (czyli używać funkcji `next()`).
- Funkcja powinna być przygotowana na przechwycenie wyjątku StopIteration. Należy zastosować blok `try-except`.
- Funkcji nie wolno odczytywać atrybutu `_cards` obiektu `deck`.
- Dołączony kod rozlosowujący karty wśród czterech graczy nie jest brany pod uwagę i można go modyfikować do woli. W swoim założeniu ma pokazywać, sytuację w której dla czwartego gracza nie starcza kart.
