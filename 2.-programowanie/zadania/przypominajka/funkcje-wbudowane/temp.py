from random import randint, random, choice
from string import ascii_letters, digits


linijka = '[0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17]\n'
linijka_po_strip = linijka.strip('[]\n')
linijka_po_strip_i_po_split = linijka_po_strip.split(', ')
lista_numerow = list(map(int, linijka_po_strip_i_po_split))

print(f'linijka: {linijka}, typ: {type(linijka)}')
print(f'linijka_po_strip: {linijka_po_strip}, typ: {type(linijka_po_strip)}')
print(f'linijka_po_strip_i_po_split: {linijka_po_strip_i_po_split}, typ: {type(linijka_po_strip_i_po_split)}')
print(f'lista_numerow: {lista_numerow}, typ: {type(lista_numerow)}')

