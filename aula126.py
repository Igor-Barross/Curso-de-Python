# __dict__ e vars para atributos de instância
class Pessoa:
    ano_atual = 2025

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimetno(self):
        return Pessoa.ano_atual - self.idade


dados = {'nome': 'Igor', 'idade': 19}
p1 = Pessoa(**dados)
# p1.__dict__['outra'] = 'coisa'
# p1.__dict__['nome'] = 'eita'
# del p1.__dict__['nome']
# print(p1.__dict__)
# print(vars(p1))
# print(p1.outra)
# print(p1.nome)
print(vars(p1))
