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
