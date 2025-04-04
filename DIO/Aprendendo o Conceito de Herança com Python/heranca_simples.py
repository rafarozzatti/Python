# Definição da classe base Veiculo
class Veiculo:
    # Método construtor (__init__) que inicializa os atributos do veículo
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor                  # Cor do veículo
        self.placa = placa              # Placa do veículo
        self.numero_rodas = numero_rodas # Quantidade de rodas do veículo

    # Método para ligar o motor do veículo
    def ligar_motor(self):
        print('Ligando o motor')

    # Método especial __str__ para representar o objeto como string quando for impresso
    def __str__(self):
        # Retorna uma string contendo o nome da classe e seus atributos formatados
        return f'{self.__class__.__name__}: {", ".join([f"{chave}: {valor}" for chave, valor in self.__dict__.items()])}'

# Definição da classe Motocicleta, que herda de Veiculo
class Motocicleta(Veiculo):
    pass  # Não adiciona nenhum comportamento novo, apenas herda de Veiculo

# Definição da classe Carro, que herda de Veiculo
class Carro(Veiculo):
    pass  # Também herda todo o comportamento da classe Veiculo

# Definição da classe Caminhao, que herda de Veiculo
class Caminhao(Veiculo):
    # Método construtor que adiciona um novo atributo: carregado
    def __init__(self, cor, placa, numero_rodas, carregado):
        # Chama o construtor da classe base (Veiculo) usando super()
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado  # Define se o caminhão está carregado ou não

    # Método para informar se o caminhão está carregado
    def esta_carregado(self):
        print(f'{"Sim" if self.carregado else "Não"} estou carregado')

# Criação de instâncias das classes
moto = Motocicleta('preta', 'abc-1234', 2)       # Criando uma moto com cor preta, placa 'abc-1234' e 2 rodas
carro = Carro('branco', 'xde-0098', 4)          # Criando um carro com cor branca, placa 'xde-0098' e 4 rodas
caminhao = Caminhao('roxo', 'gfd-8712', 8, True) # Criando um caminhão roxo, placa 'gfd-8712', 8 rodas e carregado

# Impressão das instâncias
print(moto)     # Exibe os atributos da motocicleta
print(carro)    # Exibe os atributos do carro
print(caminhao) # Exibe os atributos do caminhão
