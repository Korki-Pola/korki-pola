start = 0.0
end = 1.0

grade = 0.0
input_incorrect = True
while input_incorrect:
    try:
        grade = float(input(f"Podaj ocene od {start} do {end}: "))

        if grade < start or grade > end:
            raise TypeError

        input_incorrect = False
    except ValueError:
        print("Musisz podac liczbe w formacie x.y (zmiennoprzecionkowa)!")
    except TypeError:
        print(f"Musisz podac liczbe w przedziale od {start} do {end}!")

if grade >= 0.9:
    print("A")
elif grade >= 0.8:
    print("B")
elif grade >= 0.7:
    print("C")
elif grade >= 0.6:
    print("D")
else:
    print("F")
