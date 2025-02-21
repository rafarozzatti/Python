from datetime import date

class Pessoa:

    def __init__(self, nome: str, data_nascimento: date, email: str) -> None:
        self.__nome: str = nome
        self.__data_nascimento: date = data_nascimento
        self.__email: str = email

    @property
    def nome(self) -> str:
        return self.__nome
    
    @nome.setter
    def nome(self, nome: str) -> None:
        self.__nome = nome

    @property
    def data_nascimento(self) -> date:
        return self.__data_nascimento
    
    @data_nascimento.setter
    def data_nascimento(self, data_nascimento: date) -> None:
        self.__data_nascimento = data_nascimento

    @property
    def email(self) -> str:
        return self.__email
    
    @email.setter
    def email(self, email: str) -> None:
        self.__email = email

    def imprimir(self) -> None:
        print(f'Nome: {self.nome}')
        print(f'E-mail: {self.email}')
        print(f'Data Nascimento: {self.data_nascimento.strftime("%d/%m/%y")}')

p1 = Pessoa('Rafael', date(year=1999, month=2, day=17), 'user@gmail.com')
p1.imprimir()
