# Ogolne notatki

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
