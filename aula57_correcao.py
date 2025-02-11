import os

lista = []

while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: ').lower()
    
    if opcao == 'i':
        os.system('cls')
        valor = input('Valor: ')
        lista.append(valor)
        
    elif opcao == 'a':
        indice_str = input('Escolha o indice para apagar: ')
        
        try:
            indice = int(indice_str)
            del lista(indice)
        except ValueError:
            print('Por favor digite apenas numeros inteiros.')
        except IndexError:
            print('Indice não existe na lista.')
        except Exception:
            print('Error desconhecido.')
            
    elif opcao == 'l':
        os.system('cls')
        
        if len(lista) == 0:
            print('Nada para listar.')
        
        for i, valor in enumerate(lista):
            print(i, valor)
            
    else:
        print('Por favor, escolha i, a ou l.')
        