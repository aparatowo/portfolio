# Zadanie domowe 0303

W tym zadaniu należy napisać generator `counter_generator`, który będzie działał jak automat wydający numerki w urzędzie, czyli:
- będzie zwracał typ `string`, który będzie kolejną liczbą naturalną:
    - każdy string będzie się składać z dwóch cyfr. W przypadku liczb jednocyfrowych należy wypełnić miejsce po lewej stronie zerem.
    - pierwszą liczbą jest `00` lub liczba przekazana do parametru `start`
- po wydaniu numerka `99` należy zacząć od początku, czyli od `00`


## Podpowiedź:
- możesz wykorzystać metodę `zfill()`: https://docs.python.org/3.8/library/stdtypes.html#str.zfill
- operator zwracający resztę z dzielenia to `%`

## Rozszerzenie:
- dodaj do `counter_generator()` parametr `digits`, który przyjmie ilość cyfr, jakie ma mieć generowany numerek. Aby testy działały dla rozszerzenia, ustaw domyślną wartość `digits` na `2`.
