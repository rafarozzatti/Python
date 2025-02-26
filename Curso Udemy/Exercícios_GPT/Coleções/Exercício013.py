"""Utilize DefaultDict para armazenar um cadastro de pessoas onde as chaves são as idades e os valores são listas com os nomes das pessoas daquela idade. Permita adicionar novos cadastros dinamicamente."""

from collections import defaultdict

cadastro = defaultdict(list)

while True:
    nome = input("Digite o nome (ou 'sair' para encerrar): ")
    if nome.lower() == 'sair':
        break
    idade = int(input("Digite a sua idade: "))
    
    cadastro[idade].append(nome)

print(cadastro)
