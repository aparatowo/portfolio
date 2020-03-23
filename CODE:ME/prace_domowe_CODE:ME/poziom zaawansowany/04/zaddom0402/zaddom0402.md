# Zadanie domowe 0402

W tym zadaniu należy napisać funkcję `generate_email_addresses()`, która każdej osobie z przekazanej listy przypisze adres email w danej domenie. Funkcja ma spełniać poniższe założenia:

- funkcja będzie przyjmować listę danych osobowych (o strukturze takiej jak lista `people` w szablonie)
- funkcja będzie zwracać **słownik** stworzony zgodnie z poniższymi zasadami:
    - kluczami słownika mają być wartości `id` każdego użytkownika
    - dla każdej wartości `id` ma być przypisany adres emailowy dla odpowiadającego temu identyfikatorowi użytkownika. Adres email tworzony jest w następujący sposób:
        - pierwszym znakiem jest pierwsza litera imienia
        - kolejnymi znakami są wszystkie litery nazwiska
        - następnie następuje znak `@` oraz nazwa domeny
        - wszystkie znaki są małymi literami
        - (jako **rozszerzenie** można zamienić polskie znaki (np. ą, ł, ć) na ich odpowiedniki w ASCII)
    - adres email ma być tworzony tylko dla użytkowników, którzy mają klucz `active` ustawiony na `True`

## Wymagania techniczne:
- W rozwiązaniu **musi** pojawić się co najmniej jedno **dict comprehension**.
