#Projekt goście
##Rafał Nitychoruk, 09.11.2019r.
###Środowisko
Python 3.7, kodowanie UTF-8, wykorzystane moduły: math, random, json, 

###Założenia programu
Program ma za zadanie przyjąć listę gosci weselnych i przetworzyć tak, by uzyskać jak największe zadowolenie wszystkich zaproszonych.
Dzieli listy na gości z osobą towarzyszącą i te samotne, dokonuje podziału na stoliki i informuje o łącznej liczbie dzieci.

Program przelosowuje listy gości i wykonuje swoją pracę przydziału do stołów 1000x. Za każdym razem sprawdza poziom zadowolenia i odnotowuje go. Na tej podstawie określa listę losowań, w której znajdują się listy stołów z maksymalnym poziomem satysfakcji. 
Następnie program wybiera z listy optymalych losowań jedną listę stołów dla par i jedną listę dla singli.

Na końcu program umożliwia podgląd listy gości i zapis do '.json'


###Uruchomienie programu
Program wymaga dwóch list gości w formacie CSV. W tej chwili powinny się znajdować w folderze, w  którym jest program.
Efektem diałania programu jest wydrukowana lista stołów dla par, osobna lista stołów dla singli i plik '.json'.

###Listy gości
Program pobiera listę gości zgodną z szablonem 'lista_gosci_szablon.csv'.
Z uwagi na planowane rozszerzenie funkcjonalności, osobno należy podać listę gości Pana i Panny Młodych.

#####Prośby
Pola 'prosba tak' i 'prosba nie' przeznaczone są na uwagi odnośnie tego z kim gość chce siedzieć, a także z kim siedzieć nie chce. Aby ta funkcjonalność zadziałała, pole to musi gadzać się w 100% z którąś wartością wpisaną w polu 'imie i nazwisko'.
#####Dzieci
Pole 'dzieci' zadziała gdy wpisana wartość będzie cyfrą.
#####Osoby samotne i starsze
Single wybierani są poprzez brak wypełnienia pola 'osoba towarzyszaca'. Pole 'osoba starsza' działa przy wartości "tak".
W tej chwili brak dodatkowej logiki działań z osobami starszymi. To pole jest jedynie informacją na temat gościa, jednak przygotowaną do dalszego rozwoju.

#####Rozpakowanie i return
Program pominie pierwszy wiersz z szablonu. Nie należy go usuwać. Pola mają pewną tolerancję wpisywanych wartości.
Za odczyt i podstawowe przetworzenie list odpowiada funkcja 'rozpakowanie_pliku' w 'lista_gosci.py', która zwraca listę obiektów 'Gosc'.




