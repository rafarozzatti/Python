opcao = int(input('Informe uma opcção: [1] Sacar \n[2] Extrato: '))

# Se opção foi 1, saque
if opcao == 1:
    valor = float(input('Informe a quantia para saque: '))
# Se opção foi 2, extrato
elif opcao == 2:
    print('Exibindo o extrato...')
# Se opção não for 1 ou 2, imprime 'Opção invalida'
else:
    print('Opção invalida')
