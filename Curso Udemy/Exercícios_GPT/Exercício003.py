"""Peça a idade do usuário e verifique se ele pode entrar na festa. As regras são:

- Menores de 18 anos não podem entrar.
- Idades entre 18 e 21 anos precisam de autorização.
- Maiores de 21 anos podem entrar livremente."""

idade = int(input('Digite sua idade: '))
if idade < 18:
    print('Você não pode entrar.')
elif idade > 21:
    print('Você pode entrar.')
else:
    print('Você pode entrar apenas com autorização.')
