# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela

class Carro:
    def __init__(self, nome) -> None:
        self.nome = nome
        self._motor = None
        self._fabricante = None

    @property
    def motor_carro(self):
        return self._motor

    @motor_carro.setter
    def motor_carro(self, motor):
        self._motor = motor

    @property
    def fabricante_carro(self):
        return self._fabricante

    @fabricante_carro.setter
    def fabricante_carro(self, fabricante):
        self._fabricante = fabricante


class Motor:
    def __init__(self, nome):
        self.nome = nome

class Fabricante:
    def __init__(self, nome):
        self.nome = nome


# Primeiro fabricante
volws = Fabricante('Volws')

# Primeiro carro
fusca = Carro('Fusca')
v8 = Motor('v8')
fusca.motor_carro = v8
fusca.fabricante_carro = volws

# Segundo carro
gol = Carro('Gol')
v12 = Motor('v12')
gol.motor_carro = v12
gol.fabricante_carro = volws

# Terceiro carro
palio = Carro('Palio')
fiat = Fabricante('Fiat')
palio.motor_carro = v8
palio.fabricante_carro = fiat


print(f'Carro: {fusca.nome}')
print(f'Motor: {fusca.motor_carro.nome}')
print(f'Fabricante: {fusca.fabricante_carro.nome}')
print()

print(f'Carro: {gol.nome}')
print(f'Motor: {gol.motor_carro.nome}')
print(f'Fabricante: {gol.fabricante_carro.nome}')
print()

print(f'Carro: {palio.nome}')
print(f'Motor: {palio.motor_carro.nome}')
print(f'Fabricante: {palio.fabricante_carro.nome}')
print()