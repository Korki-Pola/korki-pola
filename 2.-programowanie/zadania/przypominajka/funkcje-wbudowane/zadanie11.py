## Zadanie 11: Funkcje `open` i `write`

# **Cel:** Zapisz string do pliku tekstowego.

string = 'fkdfnmksd\nasdlfkjasdlfj asdlfkjasdlfkj\nasdlfjasldkfj'

with open('./zadanie11_output.txt', 'w') as file:
    file.write(string)
