x = input('Podaj mi swoje pierwsze imie: ')
y = input("Podaj mi swoje nazwisko: ")
z = input("Podaj mi swoje drugie imie: ")
s = ' '
n = '|'
text = f'{n}{s}{x}{s}{n}'
text_2 = f'{n}{s}{y}{s}{n}'
text_3 = f'{n}{s}{z}{s}{n}'

imie = "IMIE"
nazwisko = "NAZWISKO"
drugie_imie = "DRUGIE_IMIE"

szerokosc_imie = 12
szerokosc_nazwisko = 14
szerokosc_d_imie = 3

print('-' * 33)
print(f'|{imie:^{szerokosc_imie}}|{nazwisko:^{szerokosc_nazwisko}}|{drugie_imie:^{szerokosc_d_imie}}|')
print(f'|{text:^{szerokosc_imie}}|')
print(f'|{text:^{szerokosc_nazwisko}}|')
print(f'|{text:^{szerokosc_d_imie}}|')
print('-' * 33)
