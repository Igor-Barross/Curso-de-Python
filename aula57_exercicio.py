import os

lista_compras = []
opcao = ''

while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: ').lower()
    
    # Verificação para saber se o usuario digitou uma opção correta
    if opcao not in 'ial':
        os.system('cls')
        print('Por favor, digite uma opção correta.')
    
    # verificação para saber se é possivel listar 
    if opcao == 'l' and lista_compras == []:
        os.system('cls')
        print('Nada a listar.')
    
    # listagem da os indices e itens da lista
    if opcao == 'l' and lista_compras != []:
        os.system('cls')
        for indice, item in enumerate(lista_compras):
            print(indice, item)
    
    # verificação para saber se é possivel apagar 
    if opcao == 'a' and lista_compras == []:
        os.system('cls')
        print('Nada a apagar.')
    
    # Apagando itens da lista
    if opcao == 'a' and lista_compras != []:
        try:
            indice_removido = int(input('Escolha um indice para apagar: '))
            lista_compras.pop(indice_removido)
            os.system('cls')
            
        except Exception:
           print('Não é possivel apagar esse indice') 
    
    # Adicionando itens da lista
    if opcao == 'i':
        os.system('cls')
        valor = input('Valor: ').capitalize()
        lista_compras.append(valor)
        os.system('cls')


            
            

    