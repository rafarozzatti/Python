def soma(*args):
    return sum(args)


print(soma(1))
print(soma(2, 3))
print(soma(2, 3, 4))
print(soma(3, 4, 5, 6))
numeros = [1, 2, 3, 4, 5, 6, 7]
print(soma(*numeros))
print()


def soma2(nome, email, *args):
    return sum(args)

print(soma2('Angelina', 'Jolie'))
print(soma2('Angelina', 'Jolie', 1))
print(soma2('Angelina', 'Jolie', 2, 3))
print(soma2('Angelina', 'Jolie', 2, 3, 4))
print(soma2('Angelina', 'Jolie', 3, 4, 5, 6))
print()


def verificar(*args):
    if 'Geek' in args and 'University' in args:
        return 'Bem-vindo Geek!'
    return 'Eu não tenho certeza quem você é...'


print(verificar(1))
print(verificar(1, True, 'University', 'Geek'))
print(verificar(1, 'University', 3.1451))
