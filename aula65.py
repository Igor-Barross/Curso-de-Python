"""
Introdução as funções (def) em Python
funções são trechos de codigos usados para
replicar determinada ação ao longo do codigo
Elas poodem receber valores para parâmetros (argumentos)
e retonrar um valor especifico
Por padrão, funções Python retornam None (nada)
"""

# def Print(a, b, c):
#     print('Varias1')
#     print('Varias2')
#     print('Varias3')

# def imprimir(a, b, c):
#     print(a, b, c)

# imprimir(1, 2, 3)
# imprimir(4, 5, 6)

def saudacao(nome= 'Sem nome'):
    print(f'Ola, {nome}!')
    
saudacao('Igor')
saudacao('Gaby')
saudacao()