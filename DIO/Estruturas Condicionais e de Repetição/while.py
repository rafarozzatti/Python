opcao = 1

# Enquanto opção for diferente de 0
while opcao != 0:
    opcao = int(input('[1] Sacar \n[2] Extrato \n[0] Sair \n Opção:'))

    if opcao == 1:
        print('Sacando...')
    elif opcao == 2:
        print('Exibindo o extrato...')
print('Obrigado por usar nosso sistema bancário, até logo!')
