"""Verifique se uma idade informada permite votar (idade mínima de 16 anos)."""

idade = int(input('Digite sua idade: '))
print(f'Você tem {idade} anos, já pode votar' if idade >= 16 else f'Você tem {idade} anos, só podera votar daqui {16 - idade} ano(s)')
