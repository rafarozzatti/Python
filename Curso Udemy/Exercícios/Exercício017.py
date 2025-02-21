from datetime import date
from Exercício016 import Pessoa

class Agenda:
    def __init__(self):
        self.__contato: list[Pessoa] = []

    @property
    def contatos(self) -> list[Pessoa]:
        return self.__contato
    
    def armazenar_contato(self, contato: Pessoa) -> None:
        self.contatos.append(contato)

    def remover_contato(self, contato: Pessoa):
        self.contatos.remove(contato)

    def busca_contato(self, nome: str) -> None:
        for indice, contato in enumerate(self.contatos):
            if contato.nome == nome:
                print(f'O contato {nome} está na posição {indice}')

    def imprimir_agenda(self) -> None:
        for contato in self.contatos:
            contato.imprimir()

    def imprimir_contato(self, indice: int) -> None:
        self.contatos[indice].imprimir()

if __name__ == '__main__':
    contato1: Pessoa = Pessoa('Rafael', date(1999, 2, 17), 'user@gmail.com')
    contato2: Pessoa = Pessoa('Enzo', date(2009, 1, 1), 'user@gmail.com')
    contato3: Pessoa = Pessoa('Aydana', date(1975, 5, 25), 'user@gmail.com')

    agenda: Agenda = Agenda()

    agenda.armazenar_contato(contato1)
    agenda.armazenar_contato(contato2)
    agenda.armazenar_contato(contato3)
    agenda.imprimir_agenda()
    agenda.busca_contato('Enzo')
    agenda.imprimir_contato(2)
    agenda.remover_contato(contato3)
    agenda.imprimir_agenda()
    