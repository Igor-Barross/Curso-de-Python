# Entendendo self em classes Python
# Classe - Molde (geralmente sem dados)
# Instância da class (objeto) - Tem os dados
# Uma classe pode gerar várias instâncias.
# Na classe o self é a própria instância.

class Carro:
    def __init__(self, nome):
        self.nome = nome

    def aceletar(self):
        print(f'{self.nome} está acelerando...')


string = 'Luiz'
print(string.upper())


fusca = Carro('fusca')
print(fusca.nome)
fusca.aceletar()

celta = Carro('celta')
print(celta.nome)
fusca.aceletar()