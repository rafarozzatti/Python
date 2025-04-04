# Definição da classe base Animal
class Animal:
    # Método construtor (__init__) que recebe o número de patas como parâmetro
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas  # Define o número de patas do animal

    # Método especial __str__ para representar o objeto como string quando for impresso
    def __str__(self):
        # Retorna uma string contendo o nome da classe e seus atributos formatados
        return f'{self.__class__.__name__}: {", ".join([f"{chave}: {valor}" for chave, valor in self.__dict__.items()])}'

# Definição da classe Mamifero, que herda de Animal
class Mamifero(Animal):
    # Método construtor que adiciona um novo atributo: cor_pelo
    def __init__(self, cor_pelo, **kwargs):
        super().__init__(**kwargs)  # Passa os demais argumentos para a classe base (Animal)
        self.cor_pelo = cor_pelo    # Define a cor do pelo do mamífero

# Definição da classe Ave, que herda de Animal
class Ave(Animal):
    # Método construtor que adiciona um novo atributo: cor_bico
    def __init__(self, cor_bico, **kwars):  
        super().__init__(**kwars)  # Passa os demais argumentos para a classe base (Animal)
        self.cor_bico = cor_bico   # Define a cor do bico da ave

# Definição da classe Gato, que herda de Mamifero
class Gato(Mamifero):
    pass  # Herda todas as características de Mamifero sem modificações

# Definição da classe Ornitorinco, que herda tanto de Mamifero quanto de Ave (herança múltipla)
class Ornitorinco(Mamifero, Ave):
    pass  # Herda todas as características de Mamifero e Ave sem modificações

# Criação de um objeto da classe Gato com 4 patas e pelo preto
gato = Gato(nro_patas=4, cor_pelo='Preto')
print(gato)  # Exibe os atributos do gato

# Criação de um objeto da classe Ornitorinco com 2 patas, pelo vermelho e bico laranja
ornitorinco = Ornitorinco(nro_patas=2, cor_pelo='Vermelho', cor_bico='Laranja')
print(ornitorinco)  # Exibe os atributos do ornitorrinco
