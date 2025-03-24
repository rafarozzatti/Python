"""Peça a nota de um aluno e diga se ele está Aprovado, de Recuperação ou Reprovado."""

nota = float(input("Digite a nota do aluno: "))

status = ("APROVADO" if nota >= 7 else "REPROVADO" if nota < 5 else "RECUPERAÇÃO")

print(f'O aluno obteve nota {nota}, então está {status}')
