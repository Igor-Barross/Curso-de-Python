# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]


contador_perguntas = 0
pergntas_corretas = 0
while True:
    
    # exibição das perguntas
    print(f'Pergunta: {perguntas[contador_perguntas]['Pergunta']}')
    print('\nOpções:')
    
    # exibição das opções
    for opcao, valor in enumerate(perguntas[contador_perguntas]['Opções']):
        print(f'{opcao}) {valor}')
    
    # escolha das opções pelo usuário
    entrada_usuario = input('Escolha uma opção: ')
    try:
        # correção de string para int
        opcao_usuario = int(entrada_usuario)
    except ValueError:
        # exeção caso o usuário não tenha digitado um int (automaticamente ele erra a pergunta)
        print('Errou ❌\n')
        continue    
    
    # conferência da reposta
    try:
        if perguntas[contador_perguntas]['Opções'][opcao_usuario] == perguntas[contador_perguntas]['Resposta']:
            print('Acertou 👍\n')
            pergntas_corretas += 1
        else:
            print('Errou ❌\n')
    except IndexError:
        # exeção caso o usário digite um valor maior que o numero de indice da lista de opções (automaticamente ele erra a pergunta)
        print('Errou ❌\n')

    contador_perguntas += 1
    if contador_perguntas >= 3:
        print(f'Você acertou {pergntas_corretas}\nde {len(perguntas)} perguntas')
        break
     