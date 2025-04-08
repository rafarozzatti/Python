# Define a classe Pessoa
class Pessoa:
    def __init__(self, nome=None, idade=None):
        # Construtor da classe que recebe nome e idade
        self.nome = nome
        self.idade = idade

    # Método de classe: recebe a própria classe como primeiro argumento (cls)
    @classmethod
    def criar_de_date_nascimento(cls, ano, mes, dia, nome):
        # Calcula a idade com base no ano de nascimento (forma simples, não considera mês/dia)
        idade = 2025 - ano
        # Retorna uma nova instância de Pessoa com o nome e a idade calculada
        return cls(nome, idade)
    
    # Método estático: não recebe nem a instância (self) nem a classe (cls)
    @staticmethod
    def e_maior_idade(idade):
        # Retorna True se a idade for maior ou igual a 18, caso contrário False
        return idade >= 18

# Cria uma pessoa usando o método de classe, baseado na data de nascimento
p = Pessoa.criar_de_date_nascimento(1994, 3, 21, 'Guilherme')

# Imprime nome e idade da pessoa criada
print(p.nome, p.idade)

# Testa o método estático para verificar se a idade 18 é considerada maior de idade
print(Pessoa.e_maior_idade(18))  # True

# Testa o método estático para idade 8
print(Pessoa.e_maior_idade(8))   # False
