# 2. Programowanie

## 2.1. Wypisywanie oraz wczytywanie danych - funkcje bufora standardowego: `print` oraz `input`

### 2.1.1. Funkcja `print` (oraz troche o `format`)

`print` jest wykorzystywany do wypisywania tekstu do standardowego bufora wyjsciowego (w wiekszosc przypadkow jest to ekran lub monitor). Tekst w Pythonie jest reprezentowany przez typ `str` powszechnie nazywany **string**.

`print` posiada trzy argumenty kluczowe (ang. key-word arguments -> **kwargs**):

- `print(args, end='')`

```python
# Wypisuje "Hello!How are you?"
print("Hello", end="!") # end nadpisuje domyslny znak '\n' (koniec linii, newline, enter) wstawiany na koncu wypisywanego stringa
print("How are you?")
```

- `print(args, sep='')`

```python
# Wypisuje "Hello-world"
print("Hello", "world", sep="-") # sep nadpisuje domyslny separator argumentow (spacje)
```

- `print(args, file=f)`

```python
with open("output.txt", "w") as f: # otworzenie pliku 'output.txt' w trybie write (zapisu)
    print("Hello, world!", file=f) # przekazanie buforu pliku do funkcji print i zapisanie tekstu "Hello, world!" do pliku "output.txt"
```

Nazwa **string** wziela sie od reprezentacji tekstu w pamieci komputera. Tekst `"Ala ma kota"` komputer widzi jako lancucha znakow postaci `['A', 'l', 'a', ' ', 'm', 'a', ' ', 'k', 'o', 't', 'a']` (jednakze tak naprawde jest to ciag liczb dwojkowych o wartosciach dziesietnych `[65, 108, 97, 32, 109, 97, 32, 107, 111, 116, 97]` gdzie kazda wartosc odpowiada odpowiedniej literze - wiecej o tym [tutaj](https://www.asciitable.com/)).

Powracajac do dzialania funkcji `print` nalezy wspomniec rowniez o metodzie `format` typu `str` ktora mozna wykorzystywac na dwa sposoby:

- zapis skrocony (uproszczony w dzialaniu):

```python
x = 'memes'

print(f'{x}') # wypisze zawartosc wstawionej w string wartosci x
```

- zapis pelny:

```python
x = 'memes'

print('{}'.format(x)) # wypisze zawartosc wstawionej w string wartosci x
```

Pelny zapis `str.format(value1, value2...)` (`str` - typ, `args` - oznaczenie miejsca na wiele argumentow dokladna dokumentacja metody do znalezienia [tutaj](https://www.w3schools.com/python/ref_string_format.asp)) pozwala na wykonywanie wielu roznych trikow, oto pare przykladow:

```python
# 1. Wypisanie "Cześć, nazywam się Jan i mam 30 lat."
name = "Jan"
age = 30
print("Cześć, nazywam się {} i mam {} lat.".format(name, age))

# 2. Wypisanie "Cześć, nazywam się Jan i mam 30 lat."
print("Cześć, nazywam się {name} i mam {age} lat.".format(name="Jan", age=30))

# 3. Wypisanie "Wartość liczby pi wynosi: 3.14"
pi = 3.141592653589793
print("Wartość liczby pi wynosi: {:.2f}".format(pi)) # zapis .2f wymusza zapis liczby w formacie ...xxxx.yy (dwie liczby po przecinku)

# 4. Wypisanie "Liczba: 1,000,000"
number = 1000000
print("Liczba: {:,}".format(number))

# 5. Wypisanie:
# |    Python|
# |Python    |
# |  Python  |
text = "Python"
print("|{:>10}|".format(text))  # Wyrównanie do prawej
print("|{:<10}|".format(text))  # Wyrównanie do lewej
print("|{:^10}|".format(text))  # Wyśrodkowanie
# wartosc 10 oznacza maksymalna szerokosc powstalego stringa
```

### 2.1.2. Funkcja `input`

`input` sluzy do odczytu danych ze standardowego buforu wejsciowego (w wiekszosci przypadkow jest to klawiatura).

Przyklady uzycia:

```python
# OUTPUT
# Enter your name: John
# Hello, John!
name = input("Enter your name: ")
print("Hello, " + name + "!")

# OUTPUT
# Enter your age: 25
# You are 25 years old.
age = int(input("Enter your age: ")) # zamiana typu z str na int
print("You are " + str(age) + " years old.")

# OUTPUT
# Enter an arithmetic expression: 2 + 3 * 4
# Result: 14
result = eval(input("Enter an arithmetic expression: ")) # funkcja eval dokonuje ewaluacji wprowadzonej wartosci pod katem algebry (jezeli string wprowadzony przez uzytkownika jest poprawnym wyrazeniem matematycznym, zostanie ono wykonane i zwrocony zostanie wynik wyrazenia)
print("Result:", result)

# OUTPUT
# Enter multiple values separated by commas: apple,banana,orange
# You entered: ['apple', 'banana', 'orange']
values = input("Enter multiple values separated by commas: ").split(",") # split (z ang. rozdzielac) rozdziela wartosci stringa znajdujac znak delimitujacy i tworzy liste zaweirajaca oddzielone wartosci (inaczej, znak oddzielajacy od siebie wartosci, w tym przypadku przecinek)
print("You entered:", values)
```

## 2.2 Funkcje manipulacji danymi - `map`, `filter`, `reduce`

### 2.2.1 Funkcja `map`

Funkcja `map()` służy do aplikowania podanej funkcji do każdego elementu podanej iterowalnej struktury danych (na przykład listy). Zwraca ona nowy iterator.

#### Przykład 1: Podnoszenie każdego elementu listy do kwadratu

```python
numbers = [1, 2, 3, 4]
# Używamy funkcji map, aby podnieść każdy element listy do kwadratu
squared = map(lambda x: x**2, numbers)

# Konwersja wynikowego iteratora na listę
squared_list = list(squared)

print(squared_list)  # Output: [1, 4, 9, 16]
```

#### Przykład 2: Konwersja listy ciągów znaków na listę liczb całkowitych

```python
string_list = ["1", "2", "3", "4"]
# Używamy funkcji map, aby przekonwertować każdy ciąg znaków na liczbę całkowitą
int_list = list(map(int, string_list))

print(int_list)  # Output: [1, 2, 3, 4]
```

#### Przykład 3: Zastosowanie wielu funkcji do jednej listy

```python
numbers = [1, 2, 3, 4]
# Definiujemy dwie funkcje: jedną podnoszącą do kwadratu, a drugą podnoszącą do potęgi trzeciej
def square(x):
    return x**2

def cube(x):
    return x**3

# Używamy funkcji map, aby zastosować obie funkcje do listy
squared = list(map(square, numbers))
cubed = list(map(cube, numbers))

print(squared)  # Output: [1, 4, 9, 16]
print(cubed)    # Output: [1, 8, 27, 64]
```

### 2.2.2 Funkcja `filter`

Funkcja `filter()` służy do filtrowania elementów sekwencji. Przyjmuje dwie wartości: funkcję oraz sekwencję. Funkcja `filter()` zwraca nowy iterator zawierający tylko te elementy sekwencji, dla których funkcja zwraca wartość `True`.

#### Przyklad 1: Filtrowanie liczb parzystych z listy.

```python
# Wejście: lista liczb
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Używamy funkcji filter z lambda funkcją, która zwraca True dla liczb parzystych
even_numbers = filter(lambda x: x % 2 == 0, num_list)

# Wyjście: konwersja iteratora do listy i wydrukowanie
print(list(even_numbers))  # [2, 4, 6, 8, 10]
```

#### Przyklad 2: Filtrowanie słów o długości większej niż 5 znaków.

```python
# Wejście: lista słów
words = ["apple", "banana", "cherry", "date", "fig"]

# Używamy funkcji filter, żeby znaleźć słowa o długości większej niż 5
long_words = filter(lambda word: len(word) > 5, words)

# Wyjście: konwersja iteratora do listy i wydrukowanie
print(list(long_words))  # ['banana', 'cherry']
```

#### Przyklad 3: Filtrowanie wartości, które są typu int.

```python
# Wejście: lista wartości różnego typu
values = [1, "apple", 2.5, "banana", 3, "cherry"]

# Używamy funkcji filter, żeby znaleźć wartości będące typem int
int_values = filter(lambda val: isinstance(val, int), values)

# Wyjście: konwersja iteratora do listy i wydrukowanie
print(list(int_values))  # [1, 3]
```

### 2.2.3 Funkcja `reduce`

Funkcja `reduce()` służy do stopniowego przetwarzania elementów sekwencji w sposób kumulatywny, tak aby zredukować sekwencję do jednej skumulowanej wartości. Funkcja `reduce()` nie jest wbudowaną funkcją w Pythonie, ale można ją znaleźć w module `functools`.

#### Przykład 1: Obliczanie iloczynu wszystkich liczb w liście.

```python
from functools import reduce

# Wejście: lista liczb
numbers = [1, 2, 3, 4]

# Używamy funkcji reduce z lambda funkcją, żeby obliczyć iloczyn wszystkich liczb
product = reduce(lambda x, y: x * y, numbers)

# Wyjście: wydrukowanie wyniku
print(product)  # 24
```

#### Przykład 2: Łączenie listy ciągów znaków w jeden ciąg.

```python
from functools import reduce

# Wejście: lista słów
words = ["Hello", " ", "World", "!"]

# Używamy funkcji reduce, żeby połączyć wszystkie słowa w jedno
sentence = reduce(lambda x, y: x + y, words)

# Wyjście: wydrukowanie zdania
print(sentence)  # "Hello World!"
```

#### Przykład 3: Znalezienie największej liczby w liście.

```python
from functools import reduce

# Wejście: lista liczb
numbers = [3, 1, 7, 4, 5]

# Używamy funkcji reduce, żeby znaleźć największą liczbę
max_number = reduce(lambda x, y: x if x > y else y, numbers)

# Wyjście: wydrukowanie największej liczby
print(max_number)  # 7
```

## 2.3 Funkcje operacji na stringach - `split`, `strip|lstrip|rstrip`, `find`

### 2.3.1 Funkcja `split`

Funkcja `split()` jest metodą ciągów znaków w Pythonie, która dzieli ciąg na listę ciągów w oparciu o podany separator. Jeśli separator nie zostanie określony, domyślnie używane są białe znaki.

#### Przykład 1: Dzielenie ciągu na podstawie spacji.

```python
# Wejście: ciąg znaków
text = "Hello World!"

# Używamy metody split, aby podzielić ciąg na podstawie spacji
words = text.split()

# Wyjście: wydrukowanie listy słów
print(words)  # ['Hello', 'World!']
```

#### Przykład 2: Dzielenie ciągu na podstawie określonego separatora.

```python
# Wejście: ciąg znaków
date_string = "2023-09-14"

# Używamy metody split, aby podzielić ciąg na podstawie myślnika "-"
date_parts = date_string.split("-")

# Wyjście: wydrukowanie listy składników daty
print(date_parts)  # ['2023', '09', '14']
```

#### Przykład 3: Dzielenie ciągu na podstawie określonej liczby wystąpień separatora.

```python
# Wejście: ciąg znaków
text = "apple,banana,cherry,date,fig"

# Używamy metody split z parametrem maxsplit, żeby podzielić ciąg po pierwszych dwóch przecinkach
fruits = text.split(",", 2)

# Wyjście: wydrukowanie listy owoców
print(fruits)  # ['apple', 'banana', 'cherry,date,fig']
```

### 2.3.2 Funkcje `strip`, `lstrip` i `rstrip`

Funkcje `strip()`, `lstrip()` oraz `rstrip()` to metody ciągów znaków w Pythonie, które służą do usuwania białych znaków (lub innych określonych znaków) z ciągów.

- `strip()` usuwa białe znaki z obu końców ciągu.
- `lstrip()` usuwa białe znaki z lewej strony ciągu.
- `rstrip()` usuwa białe znaki z prawej strony ciągu.

#### Przykład 1: Używanie `strip()`, `lstrip()` i `rstrip()`.

```python
# Wejście: ciąg znaków
text = "   Hello World!   "

# Używamy metod strip, lstrip i rstrip
stripped_text = text.strip()
left_stripped_text = text.lstrip()
right_stripped_text = text.rstrip()

# Wyjście: wydrukowanie przetworzonych ciągów
print(stripped_text)  # "Hello World!"
print(left_stripped_text)  # "Hello World!   "
print(right_stripped_text)  # "   Hello World!"
```

#### Przykład 2: Usuwanie określonych znaków z ciągu.

```python
# Wejście: ciąg znaków
text = "###Hello World!###"

# Używamy metod strip, lstrip i rstrip z określonymi znakami do usunięcia
stripped_text = text.strip("#")
left_stripped_text = text.lstrip("#")
right_stripped_text = text.rstrip("#")

# Wyjście: wydrukowanie przetworzonych ciągów
print(stripped_text)  # "Hello World!"
print(left_stripped_text)  # "Hello World!###"
print(right_stripped_text)  # "###Hello World!"
```

#### Przykład 3: Praktyczne zastosowanie - usuwanie końcowego znaku nowej linii.

```python
# Wejście: ciąg znaków z końcowym znakiem nowej linii
text_with_newline = "Hello World!\n"

# Używamy metody rstrip, żeby usunąć końcowy znak nowej linii
cleaned_text = text_with_newline.rstrip("\n")

# Wyjście: wydrukowanie przetworzonego ciągu
print(cleaned_text)  # "Hello World!"
```

### 2.3.3 Funkcja `find`

Metoda `find()` dla ciągów znaków w Pythonie służy do wyszukiwania podciągu w głównym ciągu. Zwraca indeks pierwszego wystąpienia podciągu lub -1, jeśli podciąg nie zostanie znaleziony.

#### Przykład 1: Wyszukiwanie podciągu w ciągu znaków.

```python
# Wejście: ciąg znaków
text = "Hello World!"

# Używamy metody find, żeby znaleźć indeks podciągu "World"
index = text.find("World")

# Wyjście: wydrukowanie indeksu
print(index)  # 6
```

#### Przykład 2: Wyszukiwanie podciągu, który nie istnieje w głównym ciągu.

```python
# Wejście: ciąg znaków
text = "Hello World!"

# Używamy metody find, żeby znaleźć indeks podciągu "Python"
index = text.find("Python")

# Wyjście: wydrukowanie indeksu
print(index)  # -1
```

#### Przykład 3: Wyszukiwanie podciągu z określonego indeksu.

```python
# Wejście: ciąg znaków
text = "Hello World! World!"

# Używamy metody find, żeby znaleźć indeks drugiego wystąpienia "World" po indeksie 10
index = text.find("World", 10)

# Wyjście: wydrukowanie indeksu
print(index)  # 14
```

## 2.4 Funkcje i koncepty uzytkowe - `len`, `int`, `float`, `str`, `tuple`, `list`, `dict`, `with open(...) as ...`

### 2.4.1 Funkcja `len`

Funkcja `len()` w Pythonie służy do określania liczby elementów w obiekcie, takim jak lista, krotka, ciąg znaków itp. W przypadku ciągów znaków zwraca liczbę znaków w ciągu.

#### Przykład 1: Określenie długości ciągu znaków.

```python
# Wejście: ciąg znaków
text = "Hello World!"

# Używamy funkcji len, żeby określić długość ciągu
length = len(text)

# Wyjście: wydrukowanie długości
print(length)  # 12
```

#### Przykład 2: Określenie liczby elementów w liście.

```python
# Wejście: lista liczb
numbers = [1, 2, 3, 4, 5]

# Używamy funkcji len, żeby określić liczbę elementów w liście
count = len(numbers)

# Wyjście: wydrukowanie liczby elementów
print(count)  # 5
```

#### Przykład 3: Określenie liczby kluczy w słowniku.

```python
# Wejście: słownik z nazwami owoców i ich kolorami
fruits = {"apple": "red", "banana": "yellow", "grape": "purple"}

# Używamy funkcji len, żeby określić liczbę kluczy w słowniku
keys_count = len(fruits)

# Wyjście: wydrukowanie liczby kluczy
print(keys_count)  # 3
```

### 2.4.2 Funkcja `int`

Funkcja `int()` w Pythonie jest używana do konwersji określonej wartości na typ całkowity (`integer`). Może być używana do konwersji zarówno ciągów znaków, jak i liczb zmiennoprzecinkowych na wartości całkowite. Można także podać bazę dla konwersji liczbowej, jeśli źródłowa wartość jest ciągiem.

#### Przykład 1: Konwersja ciągu znaków na liczbę całkowitą.

```python
# Wejście: ciąg znaków reprezentujący liczbę
text_number = "123"

# Używamy funkcji int, żeby przekształcić ciąg znaków na liczbę całkowitą
number = int(text_number)

# Wyjście: wydrukowanie liczby całkowitej
print(number)  # 123
```

#### Przykład 2: Konwersja liczby zmiennoprzecinkowej na liczbę całkowitą.

```python
# Wejście: liczba zmiennoprzecinkowa
float_number = 12.7

# Używamy funkcji int, żeby przekształcić liczbę zmiennoprzecinkową na liczbę całkowitą
integer_number = int(float_number)

# Wyjście: wydrukowanie liczby całkowitej (część ułamkowa zostaje obcięta)
print(integer_number)  # 12
```

#### Przykład 3: Konwersja ciągu znaków na liczbę całkowitą z określoną bazą.

```python
# Wejście: ciąg znaków reprezentujący liczbę w bazie 16 (szesnastkowej)
hex_number = "1a"

# Używamy funkcji int z określoną bazą, żeby przekształcić ciąg znaków na liczbę całkowitą
decimal_number = int(hex_number, 16)

# Wyjście: wydrukowanie liczby całkowitej w bazie dziesiętnej
print(decimal_number)  # 26
```

### 2.4.3 Funkcja `float`

Funkcja `float()` w Pythonie jest używana do konwersji określonej wartości na typ zmiennoprzecinkowy (`float`). Może być używana do konwersji zarówno ciągów znaków, jak i liczb całkowitych na wartości zmiennoprzecinkowe.

#### Przykład 1: Konwersja ciągu znaków na liczbę zmiennoprzecinkową.

```python
# Wejście: ciąg znaków reprezentujący liczbę
text_number = "123.45"

# Używamy funkcji float, żeby przekształcić ciąg znaków na liczbę zmiennoprzecinkową
number = float(text_number)

# Wyjście: wydrukowanie liczby zmiennoprzecinkowej
print(number)  # 123.45
```

#### Przykład 2: Konwersja liczby całkowitej na liczbę zmiennoprzecinkową.

```python
# Wejście: liczba całkowita
int_number = 12

# Używamy funkcji float, żeby przekształcić liczbę całkowitą na liczbę zmiennoprzecinkową
float_number = float(int_number)

# Wyjście: wydrukowanie liczby zmiennoprzecinkowej
print(float_number)  # 12.0
```

#### Przykład 3: Konwersja innego ciągu znaków na liczbę zmiennoprzecinkową.

```python
# Wejście: ciąg znaków reprezentujący liczbę w notacji naukowej
sci_number = "1.23e4"

# Używamy funkcji float, żeby przekształcić ciąg znaków w notacji naukowej na liczbę zmiennoprzecinkową
converted_number = float(sci_number)

# Wyjście: wydrukowanie liczby zmiennoprzecinkowej
print(converted_number)  # 12300.0
```

### 2.4.4 Funkcja `str`

Funkcja `str()` w Pythonie jest używana do konwersji określonej wartości na typ ciągu znaków (`string`). Może być używana do konwersji wielu różnych typów danych, takich jak liczby całkowite, liczby zmiennoprzecinkowe, listy i innych na ciągi znaków.

#### Przykład 1: Konwersja liczby całkowitej na ciąg znaków.

```python
# Wejście: liczba całkowita
int_number = 123

# Używamy funkcji str, żeby przekształcić liczbę całkowitą na ciąg znaków
text_number = str(int_number)

# Wyjście: wydrukowanie ciągu znaków
print(text_number)  # "123"
```

#### Przykład 2: Konwersja liczby zmiennoprzecinkowej na ciąg znaków.

```python
# Wejście: liczba zmiennoprzecinkowa
float_number = 12.34

# Używamy funkcji str, żeby przekształcić liczbę zmiennoprzecinkową na ciąg znaków
text_number = str(float_number)

# Wyjście: wydrukowanie ciągu znaków
print(text_number)  # "12.34"
```

#### Przykład 3: Konwersja listy na ciąg znaków.

```python
# Wejście: lista liczb
numbers = [1, 2, 3, 4, 5]

# Używamy funkcji str, żeby przekształcić listę na ciąg znaków
text_list = str(numbers)

# Wyjście: wydrukowanie ciągu znaków
print(text_list)  # "[1, 2, 3, 4, 5]"
```

### 2.4.5 Funkcja `tuple`

Funkcja `tuple()` w Pythonie jest używana do konwersji określonej wartości lub sekwencji na krotkę (`tuple`). Krotki są niemodyfikowalnymi sekwencjami, które mogą przechowywać różne typy elementów.

#### Przykład 1: Konwersja listy na krotkę.

```python
# Wejście: lista liczb
numbers_list = [1, 2, 3, 4, 5]

# Używamy funkcji tuple, żeby przekształcić listę na krotkę
numbers_tuple = tuple(numbers_list)

# Wyjście: wydrukowanie krotki
print(numbers_tuple)  # (1, 2, 3, 4, 5)
```

#### Przykład 2: Konwersja ciągu znaków na krotkę.

```python
# Wejście: ciąg znaków
text = "python"

# Używamy funkcji tuple, żeby przekształcić ciąg znaków na krotkę
text_tuple = tuple(text)

# Wyjście: wydrukowanie krotki
print(text_tuple)  # ('p', 'y', 't', 'h', 'o', 'n')
```

#### Przykład 3: Utworzenie pustej krotki.

```python
# Używamy funkcji tuple, żeby utworzyć pustą krotkę
empty_tuple = tuple()

# Wyjście: wydrukowanie pustej krotki
print(empty_tuple)  # ()
```

### 2.4.6 Funkcja `list`

Funkcja `list()` w Pythonie służy do konwersji określonej wartości lub sekwencji na listę (`list`). Listy są modyfikowalnymi sekwencjami, które mogą przechowywać elementy różnych typów.

#### Przykład 1: Konwersja krotki na listę.

```python
# Wejście: krotka liczb
numbers_tuple = (1, 2, 3, 4, 5)

# Używamy funkcji list, żeby przekształcić krotkę na listę
numbers_list = list(numbers_tuple)

# Wyjście: wydrukowanie listy
print(numbers_list)  # [1, 2, 3, 4, 5]
```

#### Przykład 2: Konwersja ciągu znaków na listę.

```python
# Wejście: ciąg znaków
text = "python"

# Używamy funkcji list, żeby przekształcić ciąg znaków na listę
text_list = list(text)

# Wyjście: wydrukowanie listy
print(text_list)  # ['p', 'y', 't', 'h', 'o', 'n']
```

#### Przykład 3: Utworzenie pustej listy.

```python
# Używamy funkcji list, żeby utworzyć pustą listę
empty_list = list()

# Wyjście: wydrukowanie pustej listy
print(empty_list)  # []
```

### 2.4.7 Funkcja `dict`

Funkcja `dict()` w Pythonie służy do tworzenia nowych słowników (`dictionary`). Słowniki są kolekcjami par klucz-wartość, które są modyfikowalne. Klucze w słowniku muszą być unikalne.

#### Przykład 1: Utworzenie słownika z listy krotek.

```python
# Wejście: lista krotek
items = [("name", "John"), ("age", 25), ("city", "New York")]

# Używamy funkcji dict, żeby przekształcić listę krotek na słownik
person_dict = dict(items)

# Wyjście: wydrukowanie słownika
print(person_dict)  # {'name': 'John', 'age': 25, 'city': 'New York'}
```

#### Przykład 2: Utworzenie słownika przy użyciu argumentów nazwanych.

```python
# Używamy funkcji dict z argumentami nazwanymi, żeby utworzyć słownik
person_dict = dict(name="Alice", age=30, city="London")

# Wyjście: wydrukowanie słownika
print(person_dict)  # {'name': 'Alice', 'age': 30, 'city': 'London'}
```

#### Przykład 3: Utworzenie pustego słownika.

```python
# Używamy funkcji dict, żeby utworzyć pusty słownik
empty_dict = dict()

# Wyjście: wydrukowanie pustego słownika
print(empty_dict)  # {}
```

### 2.4.8 Instrukcja `with open(...) as ...`

Instrukcja `with open(...) as ...` w Pythonie jest używana do otwierania plików w taki sposób, aby zapewnić ich poprawne zamknięcie po zakończeniu pracy z nimi. Działa to dzięki mechanizmowi kontekstu, który gwarantuje, że po opuszczeniu bloku `with`, plik zostanie automatycznie zamknięty.

#### Przykład 1: Odczyt zawartości pliku tekstowego.

```python
# Używamy instrukcji with open(...) as ..., żeby otworzyć plik do odczytu
with open('plik.txt', 'r') as file:
    content = file.read()

    # Wyjście: wydrukowanie zawartości pliku
    print(content)
```

#### Przykład 2: Zapis tekstu do pliku.

```python
# Tekst do zapisu
text = "Witaj, świecie!"

# Używamy instrukcji with open(...) as ..., żeby otworzyć plik do zapisu
with open('nowy_plik.txt', 'w') as file:
    file.write(text)

# Po opuszczeniu bloku with, plik 'nowy_plik.txt' zawiera tekst "Witaj, świecie!"
```

#### Przykład 3: Odczyt linii po linii z pliku tekstowego.

```python
# Używamy instrukcji with open(...) as ..., żeby otworzyć plik do odczytu
with open('plik.txt', 'r') as file:
    for line in file:
        print(line.strip())  # wydrukowanie linii bez dodatkowych białych znaków
```
