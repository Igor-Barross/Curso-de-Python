# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.
import json

CAMINHO_ARQUIVO = 'aula127.json'

class Pessoa():

    def __init__(self, nome, idade, peso):
        self.nome = nome
        self.idade = idade
        self.peso = peso


p1 = Pessoa('Igor', 19, 93.5)
p2 = Pessoa('Gaby', 18, 73.3)
p3 = Pessoa('Ruan', 21, 84.3)

db = [vars(p1), vars(p2), vars(p3)]

def fazer_dump():
    with open(CAMINHO_ARQUIVO, 'w', encoding='utf8') as arquivo:
        pessoa = json.dump(db, arquivo, indent=2, ensure_ascii=False)


if __name__ == '__main__':
    fazer_dump()





# import json

# CAMINHO_ARQUIVO = 'aula127.json'

# class Pessoa():

#     def __init__(self, idade, nome, peso):
#         self.idade = idade
#         self.nome = nome
#         self.peso = peso


# def add_dados(dict, caminho_arquivo):
#     dados = dict
#     with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
#             dados = json.dump(dict, arquivo, indent=2, ensure_ascii=False)
#     return dados


# p1 = Pessoa(19, 'Igor', 94.5)

# dados_pessoa = add_dados(vars(p1), CAMINHO_ARQUIVO)


