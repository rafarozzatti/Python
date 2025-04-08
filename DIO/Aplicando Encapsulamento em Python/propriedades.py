# Define uma classe chamada Foo
class Foo:
    # Método construtor que aceita um valor inicial opcional para x
    def __init__(self, x=None):
        self._x = x  # Atributo "protegido" (por convenção), armazenado como _x

    # Define uma propriedade chamada 'x'
    @property
    def x(self):
        # Retorna o valor de _x, ou 0 se _x for None ou "falsy"
        return self._x or 0

    # Define o comportamento ao fazer uma atribuição como: foo.x = valor
    @x.setter
    def x(self, value):
        # Em vez de substituir, ele soma o valor ao _x atual
        self._x += value

    # Define o comportamento ao deletar foo.x (com del)
    @x.deleter
    def x(self):
        # Reseta _x para 0
        self._x = 0

# Cria um objeto foo com _x igual a 10
foo = Foo(10)

# Imprime foo.x → retorna 10
print(foo.x)

# Deleta a propriedade x → _x vira 0
del foo.x

# Imprime foo.x → como _x agora é 0, retorna 0
print(foo.x)

# Usa o setter para somar 10 a _x (0 + 10)
foo.x = 10

# Imprime foo.x → agora deve retornar 10
print(foo.x)
