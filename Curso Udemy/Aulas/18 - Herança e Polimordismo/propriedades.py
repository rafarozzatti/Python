class Conta:

    cont = 0

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.cont
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.cont += 1

    @property
    def numero(self):
        return self.__numero
    
    @property
    def titular(self):
        return self.__titular
    
    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def limite(self):
        return self.__limite
    
    @limite.setter
    def limite(self, novo_limite):
        self.__limite = novo_limite


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

    
conta1 = Conta('Rafael', 5000, 10000)
conta2 = Conta('Enzo', 2000, 5000)
print(conta1.extrato())
print(conta2.extrato())
soma = conta1.saldo + conta2.saldo
print(f'A soma do saldo das contas é {soma}')
conta2.limite = 6000
print(conta2.extrato())
