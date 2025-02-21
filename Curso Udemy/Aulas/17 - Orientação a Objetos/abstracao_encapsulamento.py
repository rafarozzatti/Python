class Conta:

    cont = 400

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.cont
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.cont += 1

    def extrato(self):
        print(f'Saldo de {self.__saldo} do titular {self.__titular} com limite de {self.__limite}')

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor

    def sacar(self, valor):
        if self.__saldo >= valor:
            self.__saldo -= valor

    def transferir(self, valor, conta_destino):
        self.__saldo -= valor
        self.__saldo -= 10 #Taxa
        conta_destino.__saldo += valor

conta1 = Conta('Rafael', 150, 1500)
conta1.extrato()
conta1.depositar(3000)
conta1.extrato()
conta1.sacar(1150)
conta1.extrato()
print()
conta2 = Conta('Aydana', 10000, 20000)
conta2.extrato()
conta3 = Conta('Enzo', 2000, 1000)
conta3.extrato()
conta2.transferir(200, conta3)
print()
conta2.extrato()
conta3.extrato()
