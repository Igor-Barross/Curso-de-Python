# Atributos de classe
class Pessoa:
    ano_atual = 2025
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    
    def get_ano_nascimetno(self):
        return Pessoa.ano_atual - self.idade
    
    
p1 = Pessoa('Igor', 19)
p2 = Pessoa('Gaby', 18)

print(Pessoa.ano_atual)
# Pessoa.ano_atual = 1

print(p1.get_ano_nascimetno())
print(p2.get_ano_nascimetno())