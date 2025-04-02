# Criando a função exibir_mensagem
def exibir_mensagem():
    print('Olá mundo!')

# Criando a função exibir_mensagem_2
def exibir_mensagem_2(nome):
    print(f'Seja bem vindo {nome}!')

# Criando a função exibir_mensagem_3
def exibir_mensagem_3(nome='Anônimo'):
    print(f'Seja bem vindo {nome}!')

# Chamando a função exibir_mensagem
exibir_mensagem()

# Chamando a função exibir_mensagem_2 com um valor
exibir_mensagem_2(nome='Rafael')

# Chamando a função exibir_mensagem_3 sem um valor
exibir_mensagem_3()

# Chamando a função exibir_mensagem_3 com um valor
exibir_mensagem_3(nome='Enzo')


# Criando a função calcular_total
def calcular_total(numeros):
    return sum(numeros)

# Criando a função retorna_antecessor_sucessor
def retorna_antecessor_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1
    return antecessor, sucessor

# Imprime a soma da lista fornecida
print(calcular_total([10, 20, 34]))

# Imprime o antecessor e o sucessor do numero fornecido
print(retorna_antecessor_sucessor(10))
