conta_normal = True
conta_universitaria = False
saldo = 2000
saque = 500

# Se conta for normal
if conta_normal:
    # Se saldo for maior ou igual, imprime 'Realizando saque!'
    if saldo >= saque:
        print('Saque realizado com sucesso!')
    # Se não, imprime 'Saque realizado com uso do cheque especial!'
    else:
        print('Saque realizado com uso do cheque especial!')
# Se conta for universitaria
elif conta_universitaria:
    # Se saldo for maior ou igual, imprime 'Realizando saque!'
    if saldo >= saque:
        print('Saque realizado com sucesso!')
    # Se não, imprime 'Saldo insuficiente!'
    else:
        print('Saldo insuficiente!')
