# print z formatem
x = '!!!Uwaga-'
y = '- $$$'
print(f'{x}Pola Gudas{y}\n', '{}17{}'.format(x, y), sep='')

dots = ': '
dol = '$'
print(f'{dol}78.34{dots} Shampoo', f'{dol}28.00{dots} Fruits', f'{dol}13.10{dots} Memes', sep='\n')

p = 'Punkt '
d = '.-'
h = '-hey i\'am '
print_txt = 'print'
format_txt = '.format'
f_txt = 'f{}'
print(f'{p}1{d}{print_txt}{h}{print_txt}!',
      f'{p}2{d}{format_txt}{h}{format_txt}!',
      f'{p}3{d}{f_txt}{h}{f_txt}!',
      sep='\n')

# input i print
x = input('Ile kosztuja jablka? ')
print(f'Jablka kosztuja {x}pln')

x = input('Gdzie mieszkasz? ')
y = input('Jak sie nazywasz? ')
# print(f'Mieszkam w {x}.')
# print(f'Nazywam sie {y}.')
print(f'Mieszkam w {x}', f'Nazywam sie {y}', sep='\n')

# tworzenie piramidki
g = '*'
s = ' '
print(f'{s*3}{g*1}')
print(f'{s*2}{g*3}')
print(f'{s*1}{g*5}')
print(f'{s*0}{g*7}')
