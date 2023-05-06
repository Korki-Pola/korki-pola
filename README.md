# Ogolne notatki

## Informacje a propos matury

Matura z informatyki sklada sie z tylko czesci teoretycznej, czesc wiekszosc zadan nalezy zapisac na arkuszu, czesc w odpowiednim miejscu na komputerze egzaminacyjnym.

| Typy zadan                                                                    | Punktowanie           | Udział % punktacji w calym arkuszu |
| ----------------------------------------------------------------------------- | --------------------- | ---------------------------------- |
| zamkniete                                                                     | `1` lub `2` punkty    | ok. `10%`                          |
| otwarte - w tym pare praktycznych wymagajacych uzycia komputera (algorytmika) | od `3` do `5` punktow | ok. `90%`                          |

## Korzystanie z git'a

- Wprowadzanie zmian:
  - Przed wprowadzeniem jakiejkolwiek zmiany (czy chodzi o wyslanie zadanka czy dokonania nowych zmian w juz istniejacych plikach) nalezy stworzyc wlasnego `branch'a` (nowa wlasna tymczasowa `galaz`), kroki do odpowiedniego stworzenia danych zmian:
    - `git switch master`
    - `git pull`
    - `git checkout -b <nazwa-brancha>` (np: `git checkout -b zadanie4`)
  - Nastepnie wprowadzamy nasze zmiany (tworzenie nowego pliku wewnatrz repozytorium lub modyfikacja juz istniejacego), a nastepnie, kiedy nasze zmiany juz sa skonczone:
    - `git add --all`
    - `git commit -m "<wiadomosc>"` (np: `git commit -m "dodanie odpowiedzi do zadania 4"`)
    - `git push`
  - Po tym wszystkim dajesz mi znac ze wprowadzilas zmiany na branchu `<nazwa-brancha>` (np: `zadanie4`) i ja sobie te zmiany obczajam i daje feedback
