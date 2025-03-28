# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.
import json
from aula127_exercicio_a import CAMINHO_ARQUIVO, Pessoa, fazer_dump

fazer_dump()

with open(CAMINHO_ARQUIVO, 'r') as arquivo:
    pessoas = json.load(arquivo)
    p1 = Pessoa(**pessoas[0])
    p2 = Pessoa(**pessoas[1])
    p3 = Pessoa(**pessoas[2])

    print(vars(p1))
    print(vars(p2))
    print(vars(p3))


# import json

# CAMINHO_ARQUIVO = 'aula127.json'

# class Pessoa():

#     def __init__(self, idade, nome, peso):
#         self.idade = idade
#         self.nome = nome
#         self.peso = peso


# def use_dados(caminho_arquivo):
#     with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
#         dados = json.load(arquivo)
#     return dados




# dados_salvo = use_dados(CAMINHO_ARQUIVO)

# p2 = Pessoa(**dados_salvo)
# print(p2.idade)
# print(p2.nome)
# print(p2.peso)

