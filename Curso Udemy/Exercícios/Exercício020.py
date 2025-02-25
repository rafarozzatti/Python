from Exercício019 import Veiculo   

class Carro(Veiculo):

    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self.__portas = portas

    @property
    def portas(self):
        return self.__portas
    
    @portas.setter
    def portas(self, portas):
        self.__portas = portas

    def imprimir(self):
        super().imprimir()
        print(f'Portas: {self.__portas}')
