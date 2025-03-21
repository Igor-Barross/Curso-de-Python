# Mantendo estados dentro da Classe
class Camera:
    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando

    def filmar(self):
        if self.filmando:
            print(f'{self.nome} JÁ está filmando...')
            return
        
        print(f'{self.nome} está filmando...')
        self.filmando = True

    def parar_filmar(self):
        if not self.filmando:
            print(f'{self.nome} Não está filmando...')
            return
        
        print(f'{self.nome} está parando de filmar...')
        self.filmando = False

    def fotografar(self):
        if self.filmando:
            print(f'{self.nome} não pode fotografar filmando...')
            return
        
        print(f'{self.nome} está fotografando...')
        self.filmando = True


c1 = Camera('Megapix')
c2 = Camera('LgPix')
# c1.filmar()
# c1.filmar()
# print(c1.filmando)
# print(c2.filmando)
c1.filmar()
c1.filmar()
c1.fotografar()
c1.parar_filmar()
c1.parar_filmar()
c1.fotografar()

print()

c2.filmar()
c2.filmar()
c2.fotografar()
c2.parar_filmar()
c2.parar_filmar()
c2.fotografar()