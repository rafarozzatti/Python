"""Crie uma NamedTuple chamada Aluno, que contém os atributos nome, idade e nota. Em seguida, crie três instâncias e exiba os dados."""

from collections import namedtuple
Aluno = namedtuple('Aluno', 'nome, idade, nota')
enzo = Aluno(nome='Enzo', idade=16, nota=7)
rafael = Aluno(nome='Rafael', idade=26, nota=9)
lucas = Aluno(nome='Lucas', idade=18, nota=8)
print(f'''O aluno {enzo.nome} de {enzo.idade} anos tem nota {enzo.nota}
O aluno {rafael.nome} de {rafael.idade} anos tem nota {rafael.nota}
O aluno {lucas.nome} de {lucas.idade} anos tem nota {lucas.nota}''')
