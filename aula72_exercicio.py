

def multiplca(*args):
    multiplicador = 1
    for numeros in args:
        multiplicador *= numeros
    return multiplicador    


numeros = 1, 2, 3, 4, 5
mult = multiplca(*numeros)
print(mult)
# print(1*2*3*4*5)


def impar_par(num):
    if num % 2 == 0:
        return f'{num} é um numero par!'
    return f'{num} é um numero impar!'
    
n = impar_par(5)
print(n)