"""
split e join com list e str
split - divide uma string (list)
join - une uma string
"""

frase =     'Olha só que   , coisa interessante         '
lista_frases_cruas = frase.split(',')

lista_frase = []
for i, frase in enumerate(lista_frases_cruas):
    lista_frase.append(lista_frases_cruas[i].strip())

# print(lista_frases_cruas)
# print(lista_frase)

frases_unidas = '-'.join(lista_frase)
print(frases_unidas)

