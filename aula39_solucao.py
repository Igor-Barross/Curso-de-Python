"""
Iterando strings com while
"""

nome = 'Jose Igor'

indice = 0
novo_nome = ''

while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'-{letra}'
    indice += 1

print(novo_nome)