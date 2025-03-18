# Problema dos parâmetros mutáveis em funções Python

def adiciona_cliente(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista


cliente1 = adiciona_cliente('Luiz')
adiciona_cliente('Helena', cliente1)
adiciona_cliente('joelma', cliente1)
cliente1.append('Marcos')

cliente2 = adiciona_cliente('Carlos')
adiciona_cliente('Maria', cliente2)

cliente3 = adiciona_cliente('Gaby')
adiciona_cliente('Julia', cliente3)

print(cliente1)
print(cliente2)
print(cliente3)

