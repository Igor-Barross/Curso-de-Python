# Ordem dos decoradores
def parametros_decoraor(name):
    def decorador(func):
        print('Decorador:', name)
        
        
        def sua_nova_funcao(*args, **kwargs):
            res = func(*args, **kwargs)
            final = f'{res} {name}'
            return final
        return sua_nova_funcao
    return decorador



@parametros_decoraor(name='5')
@parametros_decoraor(name='4')
@parametros_decoraor(name='3')
@parametros_decoraor(name='2')
@parametros_decoraor(name='1')
def soma(x, y):
    return x + y


dez_mais_cinco = soma(10, 5)
print(dez_mais_cinco)