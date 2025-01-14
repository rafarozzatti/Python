n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print(f'Tirando {n1} e {n2}, a média do aluno é de {m:.1f}')
if m < 5:
    print('O aluno está REPROVADO')
elif m >= 7:
    print('O aluno está APROVADO')
else:
    print('O aluno está de RECUPERAÇÃO')