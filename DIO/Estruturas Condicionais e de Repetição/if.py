saldo = 2000.0
saque = float(input('Informe o valor do saque: '))

# Se saldo for maior ou igual, imprime 'Realizando saque!'
if saldo >= saque:
    print('Realizando saque!')

# Se saldo for menor, imprime 'Saldo insuficiente!'
if saldo < saque:
    print('Saldo insuficiente!')
