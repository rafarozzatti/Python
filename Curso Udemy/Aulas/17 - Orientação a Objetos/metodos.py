class Lampada:
    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.ligada = False


class ContaCorrente:

    cont = 4999

    def __init__(self, numero, limite, saldo):
        self.__numero = ContaCorrente.cont + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.cont = self.__numero


class Produto:

    cont = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto.cont + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.cont = self.id

    def desconto(self, porcentagem):
        return (self.__valor * (100 - porcentagem)) / 100


class Usuario:

    cont = 0

    @classmethod
    def conta_usuario(cls):
        print(f'Temos {cls.cont} usuário(s) no sistema')

    def __init__(self, nome, sobrenome, email, senha):
        self.id = Usuario.cont + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = senha
        Usuario.cont = self.id

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

p1 = Produto('PlayStation 5', 'Video game', 3500)
print(p1.desconto(20))
print()

u1 = Usuario('Rafael', 'Rozzatti', 'usergmail.com', 1234)
print(u1.nome_completo())
Usuario.conta_usuario()
