# Coletando dados
nome_usuario = (input('Qual o seu nome? ')).strip()
idade_usuario = (input('Qual a sua idade? '))

if nome_usuario and idade_usuario:
    # Exibição dos dados
    print('-' * 40)
    print(f'Seu nome é {nome_usuario}')
    print(f'Seu nome invertido é {nome_usuario[::-1]}')

    # Verificação se tem espaço ou não
    if ' ' in nome_usuario:
        print('Seu nome contém espaços')
        # Contagem de quantas letras   
        for e in nome_usuario:
            espacos = 0
            if '' in nome_usuario:
                espacos += 1
        print(f'Seu nome tem {len(nome_usuario) - espacos} letras')
    else:
        print('Seu nome não contém espaços')

    # Primeira e ultima letra

    print(f'A primeira letra do seu nome é {nome_usuario[0]}')
    print(f'A ultima letra do seu nome é {nome_usuario[-1]}')
else:
    print('Desculpe, voce deixou algum campo vazio!')




