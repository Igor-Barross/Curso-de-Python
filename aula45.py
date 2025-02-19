"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""

# texto = iter('Igor')  #__iter__()

# print(next(texto)) #__next__()
# print(next(texto))
# print(next(texto))
# print(next(texto))


# for letra in texto
texto = 'Igor' # iterável
# iteratador = iter(texto) # iterator

# while True:
#     try:
#         print(next(iteratador))
#     except StopIteration:
#         break

for letra in texto:
    print(letra)