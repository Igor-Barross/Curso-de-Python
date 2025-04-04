# super() e a sobreposição de membros - Python Orientado a Objetos
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class

# class MinhaString(str):
#     def upper(self):
#         print('CHAMOU UPPER')
#         retorno = super(MinhaString, self).upper()
#         print('DEPOIS UPPER')
#         return retorno

# string = MinhaString('Igor')
# print(string.upper())

class A:
    atributo_a = 'VALOR A'

    def __init__(self, atributo):
        self.atributo = atributo

    def metodo(self):
        print('A')


class B(A):
    atributo_b = 'VALOR B'

    def __init__(self, atributo, outra_coisa):
        super().__init__(atributo)
        self.outra_coisa = outra_coisa
    
    def metodo(self):
        print('B')


class C(B):
    atributo_c = 'VALOR C'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print('Ei, burlei o sistema')

    def metodo(self):
        super().metodo()    # B
        super(B, self).metodo() # A
        super(B, self).metodo() # object
        print('C')


# print(C.mro())
# print(B.mro())
# print(A.mro())
c = C('atributo', 'outra coisa')
print(c.atributo)
# print(c.atributo_a)
# print(c.atributo_b)
# print(c.atributo_c)
# c.metodo()