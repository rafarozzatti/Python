"""Peça duas notas e diga se o aluno passou (média ≥ 7), está em recuperação (5 ≤ média < 7) ou reprovado."""

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
if media >= 7:
    print(f'O aluno obteve média {media:.2f}, está APROVADO')
elif media < 5:
    print(f'O aluno obteve média {media:.2f}, está REPROVADO')
else:
    print(f'O aluno obteve média {media:.2f}, está de RECUPERAÇÃO')
