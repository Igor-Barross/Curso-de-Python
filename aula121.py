# Métodos em instâncias de classes Python
# Hard coded - É algo que foi escrito diretamente no código
class Carro:
    def __init__(self, nome):
        self.nome = nome

    def aceletar(self):
        print(f'{self.nome} está acelerando...')


fusca = Carro('fusca')
print(fusca.nome)
fusca.aceletar()

celta = Carro('celta')
print(celta.nome)
fusca.aceletar()
