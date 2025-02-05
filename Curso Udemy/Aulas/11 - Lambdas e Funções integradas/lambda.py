calc = lambda x: 3 * x + 1

print(calc(4))
print(calc(7))
print()


nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()

print(nome_completo(' angelina', 'JOLIE'))
print(nome_completo('   FELICITY      ', ' jones'))
print()


amar = lambda: 'Como não amar Python'
uma = lambda x: 3 * x + 1
duas = lambda x, y: (x * y) ** 0.5
tres = lambda x, y, z: 3 / (1 / x + 1 / y + 1 / z)
print(amar())
print(uma(6))
print(duas(5, 7))
print(tres(3, 6, 9))
print()


autores = ['Isaac Asinov', 'Ray Bradbury', 'Robert Heinlein', 'Artur C. Clarke', 'Frank Herbert', 'Orson Scott Card', 'Douglas Adams', 'H. G. Wes', 'Leigh Brackett']
print(autores)
autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())
print(autores)
print()


def funcao_quadratica(a, b, c):
    return lambda x: a * x ** 2 + b * x + c

teste = funcao_quadratica(2, 3, -5)
print(teste(0))
print(teste(1))
print(teste(2))
print(funcao_quadratica(3, 0, 1)(2))