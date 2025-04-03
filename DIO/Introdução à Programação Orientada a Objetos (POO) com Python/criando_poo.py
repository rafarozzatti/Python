# Definição da classe Bicicleta
class Bicicleta:
    # Método construtor que inicializa os atributos da bicicleta
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor       # Cor da bicicleta
        self.modelo = modelo # Modelo da bicicleta
        self.ano = ano       # Ano de fabricação
        self.valor = valor   # Preço da bicicleta

    # Método para simular o som da buzina da bicicleta
    def buzinar(self):
        print('Plin plin...')

    # Método para simular a parada da bicicleta
    def parar(self):
        print('''Parando bicicleta...
Bicicleta parada!''')
        
    # Método para simular a bicicleta em movimento
    def correr(self):
        print('Vrummmmmmm...')

    # Método especial que define a representação em string da bicicleta
    def __str__(self):
        # Retorna uma string formatada com os atributos da bicicleta
        return f'{self.__class__.__name__}: {", ".join([f"{chave}: {valor}" for chave, valor in self.__dict__.items()])}'

# Criando um objeto da classe Bicicleta com atributos específicos
b1 = Bicicleta('vermelha', 'caloi', 2025, 600)

# Chamando os métodos da bicicleta
b1.buzinar() # Exibe "Plin plin..."
b1.parar()   # Exibe "Parando bicicleta... Bicicleta parada!"
b1.correr()  # Exibe "Vrummmmmmm..."

# Exibindo as informações formatadas da bicicleta b1
print(f'\nModelo: {b1.modelo.title()}')  # Transforma o primeiro caractere em maiúsculo
print(f'Ano: {b1.ano}')
print(f'Cor: {b1.cor.title()}')           # Transforma o primeiro caractere em maiúsculo
print(f'Valor: R${b1.valor:.2f}')        # Exibe o valor com duas casas decimais

print() # Linha em branco para organização

# Criando outro objeto da classe Bicicleta
b2 = Bicicleta('verde', 'monark', 2000, 189)

# Chamando o método buzinar de duas formas diferentes:
Bicicleta.buzinar(b2) # Chamando diretamente pela classe e passando o objeto b2
b2.buzinar()          # Chamando pelo próprio objeto b2

# Exibindo a representação da bicicleta b2 (usa o método __str__)
print(b2)
