
def funcao(numero):
    def dobrar(numero):
        return f'{numero} dobrado = {numero * 2}'
    
    def triplicar(numero):
         return f'{numero} triplicado = {numero * 3}'
     
    def quadriplicar(numero):
         return f'{numero} quadriplicado = {numero * 4}' 
     
    return dobrar(numero), triplicar(numero), quadriplicar(numero)


numero_teste = funcao(2)
for numero in numero_teste:
    print(numero)