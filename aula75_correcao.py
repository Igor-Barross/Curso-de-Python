def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return multiplicador * numero
    return multiplicar

dobrar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadriplicar = criar_multiplicador(4)

print(dobrar(2))    
print(triplicar(2))    
print(quadriplicar(2))    
    
    