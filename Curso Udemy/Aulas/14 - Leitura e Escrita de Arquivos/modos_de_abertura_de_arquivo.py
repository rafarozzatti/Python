try:
    with open('uiversity.txt', 'x') as arquivo:
        arquivo.write('Teste de conteudo\n')
except FileExistsError:
    print('Arquivo já existe')

with open('uiversity.txt', 'a') as arquivo:
    while True:
        palavra = input('Digite uma palavra: ')
        if palavra != 'sair':
            arquivo.write(palavra)
            arquivo.write('\n')
        else:
            break
