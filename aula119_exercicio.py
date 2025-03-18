# Exercício - Lista de tarefas com desfazer e refazer
 # todo = [] -> lista de tarefas
 # todo = ['fazer café'] -> Adicionar fazer café
 # todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
 # desfazer = ['fazer café',] -> Refazer ['caminhar']
 # desfazer = [] -> Refazer ['caminhar', 'fazer café']
 # refazer = todo ['fazer café']
 # refazer = todo ['fazer café', 'caminhar']

import os

# Função para limpar tela
def limpa_tela():
    return os.system('cls')


def lisar(tarefas):
    print()
    if not tarefas:
        print('Nada a listar.')
        print()
        return    
    print('TAREFAS:')
    for tarefa in tarefas:
        print(f'\t{tarefa}')
    print()


def desfazer(tarefas, tarefas_refazer):
    print()
    if not tarefas:
        print('Nenhuma tarefa a desfazer.')
        print()
        return
    tarefa = tarefas.pop()
    print(f'{tarefa=} removida da lista de tarefas.')
    tarefas_refazer.append(tarefa)
    print()


def refazer(tarefas, tarefas_refazer):
    print()
    if not tarefas_refazer:
        print('Nenhuma tarefa a refazer.')
        print()
        return
    tarefa = tarefas_refazer.pop()
    print(f'{tarefa=} adicionada a lista de tarefas.')
    tarefas.append(tarefa)
    print()

def adicionar(tarefa, tarefas):
    print()
    tarefa = tarefa.strip()
    if not tarefa:
        print('Você não digitou uma tarefa.')
        print()
        return
    print(f'{tarefa=} adicionada a lista de tarefas')
    tarefas.append(tarefa)
    print()


tarefas = []
tarefas_refazer = []

while True:
    print('Comados: listar, desfazer, refazer, parar, clear')
    tarefa = input('Digite uma tarefa ou comando: ')
    print()
    
    if tarefa == 'listar':
        lisar(tarefas)

    elif tarefa == 'desfazer':
        desfazer(tarefas, tarefas_refazer)

    elif tarefa == 'refazer':
        refazer(tarefas, tarefas_refazer)
  

    elif tarefa == 'clear':
        limpa_tela()

    elif tarefa == 'parar':
        break
    
    else:
        adicionar(tarefa, tarefas)
        lisar(tarefas)
