# Define uma classe chamada Conta para representar uma conta bancária simples
class Conta:
    # Método construtor, inicializa o objeto com um saldo inicial
    def __init__(self, saldo):
        self._saldo = saldo  # Atributo "protegido" (por convenção) que armazena o saldo da conta

    # Método para depositar um valor na conta
    def depositar(self, valor):
        self._saldo += valor  # Soma o valor ao saldo atual

    # Método para sacar um valor da conta, com validação
    def sacar(self, valor):
        # Verifica se o valor solicitado é maior que o saldo disponível
        if valor > self._saldo:
            # Se o saldo for insuficiente, exibe uma mensagem de erro
            print(f'Erro: Saldo insuficiente para sacar R${valor:.2f}. Saldo disponível: R${self._saldo:.2f}')
        else:
            # Caso contrário, realiza o saque subtraindo o valor do saldo
            self._saldo -= valor

    # Método para mostrar o saldo atual da conta
    def mostrar_saldo(self):
        return self._saldo  # Retorna o valor do saldo atual

# Cria uma conta com saldo inicial de R$100
conta = Conta(100)

# Realiza um depósito de R$100
conta.depositar(100)  # Saldo passa a ser R$200

# Realiza um saque de R$50 (válido)
conta.sacar(50)  # Saldo agora é R$150

# Tenta realizar um saque de R$300 (inválido)
conta.sacar(300)  # Não é permitido, exibe mensagem de erro

# Exibe o saldo final da conta
print(f'Saldo final: R${conta.mostrar_saldo():.2f}')  # Deve imprimir: Saldo final: R$150.00
