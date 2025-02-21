# classes com atributos publicos
class Lampada:
    def __init__(self, voltagem , cor):
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False

class ContaCorrente:
    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo

class Produto:

    imposto = 1.05
    cont = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto.cont + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        Produto.cont = self.id

class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

# classes com atributos privados
class Acesso:
    def __init__(self, email, senha):
        self.__email = email
        self.__senha = senha

    def mostra_senha(self):
        print(self.__senha)

    def mostra_email(self):
        print(self.__email)

user = Acesso('usergmail.com', '123456')
user.mostra_email()
user.mostra_senha()
print()

p1 = Produto('PlayStation 5', 'Video game', 3500)
p2 = Produto('Xbox X', 'Video game', 3000)
print(Produto.imposto)
print(p1.valor)
print(p1.id)
print(p2.valor)
print(p2.id)
