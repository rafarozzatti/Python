"""Crie um dicionário onde as chaves são nomes de alunos e os valores são suas idades. Depois, peça para o usuário digitar um nome e exiba a idade correspondente."""

dicionario = {'Rafael': 26, 'Enzo': 16, 'Aydana': 50, 'Adriano': 51}
nome = input('Digite um nome: ')
if nome in dicionario:
    print(f'O/A {nome} tem {dicionario[nome]} anos')
else:
    print(f'O nome {nome} não está no dicionário')
