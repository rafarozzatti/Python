saldo = 2000
saque = 500

# Se saldo for maior ou igual ao saque, status = 'Sucesso', se não status = 'Falha'
status = 'Sucesso' if saldo >= saque else 'Falha'

print(f'{status} ao realizar o saque!')
