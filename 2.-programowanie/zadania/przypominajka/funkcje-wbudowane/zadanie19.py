## Zadanie 19: Kombinacja `filter` i `open`

#**Cel:** Odczytaj plik i wyświetl tylko linie zawierające słowo "Python".

#with open("./zadanie19_output.txt", "w") as output_file:
 #   with open("./zadanie19_input.txt", "r") as input_file:
  #      for linijka in input_file.readlines():
   #         if "Python" in linijka:
    #            print(linijka)

with open("./zadanie19_output.txt", "w") as output_file:
    with open("./zadanie19_input.txt", "r") as input_file:
        for linijka in input_file.readlines():
            linie_wybrane = filter(lambda linijka: "Python" in linijka, input_file)
            print(linijka)
