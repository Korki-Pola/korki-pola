x = input ('Podaj mi swoje pierwsze imie: ')
y = input ("Podaj mi swoje nazwisko: ")
z = input ("Podaj mi swoje drugie imie ")
s = ' '
n = '|'
text = f'{n}{s}{x}{s}{n}'
text_2 = f'{n}{s}{y}{s}{n}'
text_3 = f'{n}{s}{z}{s}{n}'
print('-' * 33)
print('| IMIE | | NAZWISKO | | DRUGIE IMIE |')
print('|{:^10}|'f'{text}')
print('|{:^10}|'f'{text_2}')
print('|{:^10}|'f'{text_3}')
print('-' * 33)
