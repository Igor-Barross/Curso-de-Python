""" Calculadora com while"""

# n1 = 0
# n2 = 0
# resultado = 0
# operador = ""

# while True:
#     print(f'{'-' * 40}')
#     n1 = int(input('Digite um numero: '))
#     n2 = int(input('Digite outro numero: '))
#     operador = str(input('Digite um operador (+, -, *, /) Digite "Sair" para encerrar o programa: '))
    
#     if operador == '+':
#         resultado = n1 + n2
#         print(f'O resultado da soma foi {resultado:.2f} ')
    
#     elif operador == '-':
#         resultado = n1 - n2
#         print(f'O restultado da subtração foi {resultado:.2f}')
    
#     elif operador == '*':
#         resultado = n1 * n2
#         print(f'O resultado da multiplicação foi {resultado:.2f}')
#     elif operador == '/':
#         resultado = n1 / n2
#         print(f'O resultado da divisão foi {resultado:.2f}')
    
    
#     resultado = 0
#     if operador == 'Sair':
#         print('Fim do programa!')
#         break


while True:
    numero_1 = input('Digite um numero: ')
    numero_2 = input('Digite outro numero: ')
    operador = input('Digite um operador (+-/*): ')
    
    numeros_validos = None
    num_1_float = 0
    num_2_float = 0
    
    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None
    
    if numeros_validos is None:
        print('Um ou ambos dos numeros digitados são inválidos.')
        continue
    
    operadores_permitidos = '+=-/*'
    
    if operador not in operadores_permitidos:
        print('Operador inválido')
        continue
    
    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue
    
    print('Realizando sua conta. Confira o resultado abaixo:')
    if operador == '+':
        print(f'{num_1_float} + {num_2_float} =', num_1_float + num_2_float)
    elif operador == '-':
        print(f'{num_1_float} - {num_2_float} =',num_1_float - num_2_float)        
    elif operador == '/':
        print(f'{num_1_float} / {num_2_float} =',num_1_float / num_2_float)   
    elif operador == '*':
        print(f'{num_1_float} * {num_2_float} =',num_1_float * num_2_float)
    else:
        print('Nunca deveria chegar aqui.')    
        
    sair = input('Quer sair? [s]im: ').lower().startswith('s')
    
    if sair is True:
        break