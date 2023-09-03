# 21. **Konwerter Temperatur**: Nieustannie pytaj użytkownika o wprowadzenie temperatury w Fahrenheitach
# i przelicz je na Celsjusza, aż użytkownik zdecyduje się przestać.

# Celcius = 1
# Fahrenheitach = 1
#
# while True:
#     try:
#         Fahrenheitach = float(input("Podaj temperature w Fahrenheitach (lub napisz 'b' aby zakonczyc): "))
#         if Fahrenheitach == "b":
#             break
#     except ValueError:
#         Celcius = (Fahrenheitach - 32) // 1.8000
#     if Fahrenheitach == "b":
#         print(f'Sprobuj ponownie')
#
# print(f"{Fahrenheitach} stopni Fahrenheit to {Celcius} stopni Celsjusza.")

#fahr = 1
#celcius = 1
while True:
    try:
        fahr = float(input("Podaj temperature w Fahrenheitach (lub napisz litere aby zakonczyc): "))
        celcius = (fahr - 32) // 1.8000
        print(f'{fahr} stopni Fahr. to {celcius} stopni Celsjusza.')
    except ValueError:
    #if fahr == 'b':
        break

#print(f'{fahr} stopni Fahr. to {celcius} stopni Celsjusza.')