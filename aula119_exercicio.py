# Exercício - Lista de tarefas com desfazer e refazer
 # todo = [] -> lista de tarefas
 # todo = ['fazer café'] -> Adicionar fazer café
 # todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
 # desfazer = ['fazer café',] -> Refazer ['caminhar']
 # desfazer = [] -> Refazer ['caminhar', 'fazer café']
 # refazer = todo ['fazer café']
 # refazer = todo ['fazer café', 'caminhar']

import os
import json

# Função para limpar tela
def limpa_tela():
    return os.system('cls')


def listar(tarefas):
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
    listar(tarefas)


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
    listar(tarefas)


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
    listar(tarefas)


def ler(tarefas, caminho_arquivo):
    dados = tarefas
    try:
        with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
            dados = json.load(arquivo)
        return dados
    except FileNotFoundError:
        salvar(tarefas, caminho_arquivo)


def salvar(tarefas, caminho_arquivo):
    dados = tarefas
    with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
        dados = json.dump(tarefas, arquivo, indent=2, 
            ensure_ascii=False)
    return dados


CAMINHO_ARQUIVO = 'aula119.json'
tarefas = ler([], CAMINHO_ARQUIVO)
tarefas_refazer = []

while True:
    print('Comados: listar, desfazer, refazer, parar, clear')
    tarefa = input('Digite uma tarefa ou comando: ')
    print()

    comandos = {
        'listar' : lambda: listar(tarefas),
        'desfazer' : lambda: desfazer(tarefas, tarefas_refazer),
        'refazer' : lambda: refazer(tarefas, tarefas_refazer),
        'clear' : lambda: limpa_tela(),
        'adicionar' : lambda: adicionar(tarefa, tarefas),
    }

    if tarefa == 'parar':
        break
    
    comando = comandos.get(tarefa) if comandos.get(tarefa) is not None else \
        comandos['adicionar']
    comando()
    salvar(tarefas, CAMINHO_ARQUIVO)


    # if tarefa == 'listar':
    #     lisar(tarefas)

    # elif tarefa == 'desfazer':
    #     desfazer(tarefas, tarefas_refazer)

    # elif tarefa == 'refazer':
    #     refazer(tarefas, tarefas_refazer)
  

    # elif tarefa == 'clear':
    #     limpa_tela()

    # elif tarefa == 'parar':
    #     break
    
    # else:
    #     adicionar(tarefa, tarefas)
    #     lisar(tarefas)
