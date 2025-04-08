# Define a classe Estudante
class Estudante:
    escola = 'DIO'  # Atributo de classe, compartilhado entre todas as instâncias

    def __init__(self, nome, matricula):
        self.nome = nome              # Atributo de instância
        self.matricula = matricula    # Atributo de instância

    def __str__(self):
        # Define como o objeto será impresso (string formatada com nome, matrícula e escola)
        return f'{self.nome} - {self.matricula} - {self.escola}'

# Função que imprime todos os objetos passados como argumento
def mostrar_valores(*objs):
    for obj in objs:
        print(obj)  # Usa o __str__ de cada objeto

# Cria dois estudantes com nome e matrícula
aluno_1 = Estudante('Guilherme', 1)
aluno_2 = Estudante('Giovanna', 2)

# Mostra os dados dos dois estudantes
mostrar_valores(aluno_1, aluno_2)

# Altera o valor do atributo de classe 'escola'
Estudante.escola = 'Python'

# Cria um novo estudante após a alteração do nome da escola
aluno_3 = Estudante('Chappin', 3)

# Mostra os dados de todos os estudantes novamente (os antigos e o novo)
mostrar_valores(aluno_1, aluno_2, aluno_3)
